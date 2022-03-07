from django.contrib import admin
from home.models import Vehicle
from home.models import Trip

#this line means to register\add the model 
#so the admin sees it in the admin page
admin.site.register(Vehicle)
admin.site.register(Trip)