from django.urls import URLPattern, path
from . import views

urlpatterns = [ 
    # first param is the url
    # the empty string means that it's the root route, and other routes will displayed after the (travel/)
    # the name so that to call this route in other files
    path('', views.home, name= 'home-home'),
    path('about/', views.about, name= 'about-home'),
    # path('/profile', views.Profile, name= 'profile-page'),
    # path('/registration', views.Registration, name= 'registration-page'),

]

