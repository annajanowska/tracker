from django.urls import path
from .views import DeviceAssignView, DeviceLocationView, UserLastLocationView, MapView

urlpatterns = [
    path('devices/<str:id>/assign/', DeviceAssignView.as_view(), name='device-assign'),
    path('devices/<str:id>/location/', DeviceLocationView.as_view(), name='device-location'),
    path('users/<int:id>/location/', UserLastLocationView.as_view(), name='user-last-location'),
    path('map/', MapView.as_view(), name='map'),
]