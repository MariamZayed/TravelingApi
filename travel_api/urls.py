from django.urls import path
from .views import TripList, TripDetail

app_name = 'travel_api'

urlpatterns = [
    path('<int:pk>/', TripDetail.as_view(), name='detailcreate'),# this endpoint to get certain row or trip
    path('', TripList.as_view(), name='listcreate'), #this to get/retrive all  and to post
]