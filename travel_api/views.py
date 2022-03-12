from rest_framework import generics # it's going to help us user the coming functions to CRUD
from home.models import Trip
from .serializers import TripSerializer
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission

##this class is from the documention :D
class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """
    
    message = 'Editing trip is restricted to author only.' #when exception raise up, this message will show up
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True
        # Instance must have an attribute named `user`.
        return obj.user == request.user


# Display Trips

class TripList(generics.ListAPIView):# this one to list *all* trips -obj- by anyone
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripDetail(generics.RetrieveAPIView):#show single trip -endpoint-, api/1 can read only by anyone
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


# Trip Admin CRUD

class CreateTrip(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class AdminTripDetail(generics.RetrieveAPIView): #we need to retrieve all trips to edit them, it's not the optimal thing, but we want to seperate 
    permission_classes = [permissions.IsAuthenticated]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class EditTrip(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class DeleteTrip(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer












""" Concrete View Classes #Generics Function
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
#RetrieveDestroyAPIView #this one to retrive indiviual item or delete(get & delete)
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView 
  #this one to retrive indiviual item or delete(get &update& delete) 
  # حدي بالك مش هينفع نستخدمها الا اذا عملنا لوج ان سيستم وان اليوزر الي عمل البوست مثلا هو بس الي هيعدل عليه
Used for read-write-delete endpoints to represent a single model instance.
"""

