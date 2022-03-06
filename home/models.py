from django.db import models
from users.models import NewUser
from django.utils import timezone


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)
    production_year = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True)

    #this means when you call query Vehicle.objects.all() it will appear by its vehicle_name not 'Vehicle objects (1)'\
    # You need to run the shell again to see the result
    def __str__(self): 
        return self.vehicle_name

# Class 