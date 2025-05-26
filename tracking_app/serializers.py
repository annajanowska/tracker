from rest_framework import serializers
from .models import User, Device, LocationPing

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

class DeviceSerializer(serializers.ModelSerializer):
    assigned_user = UserSerializer(read_only=True)

    class Meta:
        model = Device
        fields = ['id', 'assigned_user', 'active']

class LocationPingSerializer(serializers.ModelSerializer):
    device = serializers.SlugRelatedField(slug_field='id', queryset=Device.objects.all())

    class Meta:
        model = LocationPing
        fields = ['id', 'device', 'latitude', 'longitude', 'ping_time']
