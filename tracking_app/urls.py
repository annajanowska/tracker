from django.urls import path
from .views import DeviceAssignView, DeviceLocationView, UserLastLocationView, MapView, DeviceListView, DeviceUnassignView

urlpatterns = [
    path('devices/<str:id>/assign/', DeviceAssignView.as_view(), name='device-assign'),
    path('devices/<str:id>/location/', DeviceLocationView.as_view(), name='device-location'),
    path('users/<int:id>/location/', UserLastLocationView.as_view(), name='user-last-location'),
    path('map/', MapView.as_view(), name='map'),
    path('devices/', DeviceListView.as_view(), name='device-list'),
    path('devices/<str:id>/unassign/', DeviceUnassignView.as_view(), name='device-unassign'),
]