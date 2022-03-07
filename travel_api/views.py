from rest_framework import generics # it's going to help us user the coming functions to get post delete and so on
from home.models import Trip
from .serializers import TripSerializer


class TripList(generics.ListCreateAPIView):# this one to create or list *all* items(get and post)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripDetail(generics.RetrieveDestroyAPIView):#this one to retrive indiviual item or delete(get & delete)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

#Generics Function
""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""