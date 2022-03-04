#this file to navigate routes for different applications in the same project
from django.contrib import admin
from django.urls import path, include
from users import views as users_views 

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('home.urls')), #this is root url  
                                    #this means any url with empty url then go to the url file for home app
                                    #whenever there's a url whis 127.0.01/ -is the root-, go to the home apllication and search for the url file => url.py
                                    #include function ensure it's another application in the same project
    path('register/', users_views.register, name='register'),
    # path('api/', include('travel_api.url', namespace='travel_api')),

]
