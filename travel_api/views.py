from rest_framework import generics # it's going to help us user the coming functions to get post delete and so on
from home.models import Trip
from .serializers import TripSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, AllowAny, DjangoModelPermissionsOrAnonReadOnly,DjangoModelPermissions

##this class is from the documention :D
class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """
    message = 'Editing post is restricted to author only.' #when exception raise up, this message will show up

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `user`.
        return obj.user == request.user



class TripList(generics.ListCreateAPIView):# this one to create or list *all* items(get and post)
    permission_classes = [DjangoModelPermissions]# so adding this permission means authenticated users can view and make posts for ex
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripDetail(generics.RetrieveUpdateDestroyAPIView):# this one to edit and delete #we need the user of the post to edit or delete, not anyone else#if he visit  api/1 he can read it only
    permission_classes = [IsOwnerOrReadOnly] #this is the class we made above
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
#RetrieveDestroyAPIView #this one to retrive indiviual item or delete(get & delete)
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView 
  #this one to retrive indiviual item or delete(get &update& delete) 
  # حدي بالك مش هينفع نستخدمها الا اذا عملنا لوج ان سيستم وان اليوزر الي عمل البوست مثلا هو بس الي هيعدل عليه
Used for read-write-delete endpoints to represent a single model instance.
"""