from django.db import models
from users.models import NewUser, CustomAccountManager
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
    # def __str__(self): 
    #     return self.id


class Trip(models.Model):
    #we're going to filter it here instead of the contrller\view
    class TripObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='success')

    options = (
        ('success', 'Success'),
        ('rejected', 'Rejection'),
        ('processing', 'In-Proccess'),
    )

    src = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='processing') 
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=1)#, null=True
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, default=1)#, null=True
    objects = CustomAccountManager()  # default manager
    tripobjects = TripObjects()  # custom manager
    # tripname =tripobjects.filter(src=src,dest=dest).query

    class Meta:
        ordering = ('-created_at',) #we will publish in descending order

    # def __str__(self): 
    #     return self.tripname