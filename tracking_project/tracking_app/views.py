from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User, Device
from .serializers import DeviceSerializer, LocationPingSerializer

class DeviceAssignView(APIView):
    def post(self, request, id):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, id=user_id)
        device = get_object_or_404(Device, id=id)

        active_devices = Device.objects.filter(assigned_user=user, active=True).exclude(id=device.id)
        for d in active_devices:
            d.active = False
            d.assigned_user = None
            d.save()

        device.assigned_user = user
        device.active = True
        device.save()

        serializer = DeviceSerializer(device)
        return Response(serializer.data)

class DeviceLocationView(APIView):
    def post(self, request, id):
        device = get_object_or_404(Device, id=id)

        if not device.active or not device.assigned_user:
            return Response(
                {"error": "Device must be active and assigned to a user."},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = request.data.copy()
        data["device"] = id

        serializer = LocationPingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLastLocationView(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)

        device = user.devices.filter(active=True).first()
        if not device:
            return Response({"error": "User has no active device assigned."}, status=status.HTTP_404_NOT_FOUND)

        last_ping = device.pings.order_by('-ping_time').first()
        if not last_ping:
            return Response({"error": "No location pings found for user's device."}, status=status.HTTP_404_NOT_FOUND)

        serializer = LocationPingSerializer(last_ping)
        return Response(serializer.data)


class MapView(APIView):
    def get(self, request):
        devices = Device.objects.filter(active=True, assigned_user__isnull=False)

        result = []

        for device in devices:
            last_ping = device.pings.order_by('-ping_time').first()
            if not last_ping:
                continue

            result.append({
                "user": {
                    "id": device.assigned_user.id,
                    "name": device.assigned_user.name
                },
                "device_id": device.id,
                "latitude": last_ping.latitude,
                "longitude": last_ping.longitude,
                "timestamp": last_ping.ping_time.isoformat()
            })

        return Response(result)

class DeviceListView(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceUnassignView(APIView):
    def post(self, request, id):
        device = get_object_or_404(Device, id=id)

        device.assigned_user = None
        device.active = False
        device.save()

        serializer = DeviceSerializer(device)
        return Response(serializer.data)