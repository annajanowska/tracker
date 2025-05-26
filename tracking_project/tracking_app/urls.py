from django.urls import path
from .views import DeviceAssignView, DeviceLocationView

urlpatterns = [
    path('devices/<str:id>/assign/', DeviceAssignView.as_view(), name='device-assign'),
    path('devices/<str:id>/location/', DeviceLocationView.as_view(), name='device-location'),
]