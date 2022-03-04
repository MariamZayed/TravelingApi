from django.contrib import admin
from home.models import Vehicle as Vehicle

#this line means to register\add the model 
#so the admin sees it in the admin page
admin.site.register(Vehicle)