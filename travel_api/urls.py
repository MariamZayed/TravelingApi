from django.urls import path
from .views import TripList, TripDetail, CreateTrip, EditTrip, AdminTripDetail, DeleteTrip

app_name = 'travel_api'

urlpatterns = [
    path('<int:pk>/', TripDetail.as_view(), name='detailcreate'),# this endpoint to get certain row or trip
    path('', TripList.as_view(), name='listcreate'), #this to get/retrive all trips
    # Travel Admin URLs
    path('admin/create/', CreateTrip.as_view(), name='createtrip'),
    path('admin/edit/tripdetail/<int:pk>/', AdminTripDetail.as_view(), name='admindetailtrip'),
    path('admin/edit/<int:pk>/', EditTrip.as_view(), name='edittrip'),
    path('admin/delete/<int:pk>/', DeleteTrip.as_view(), name='deletetrip'),
]