#this file to navigate routes for different applications in the same project
from django.contrib import admin
from django.urls import path, include
from users import views as users_views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)   

urlpatterns = [ 
    #API JWT Token Management
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Project URLs
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # User Management
    path('api/user/', include('users.urls', namespace='users')),#register
    # Travel_API Application
    path('api/', include('travel_api.urls', namespace='travel_api')),
]







""" For '', include('home.urls', namespace='home')
this is root url  
this means any url with empty url then go to the url file for home app
whenever there's a url whis 127.0.01/ -is the root-, go to the home apllication and search for the url file => url.py


path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),#this to simualte login-system for user, it's just GUI for rest 
 """