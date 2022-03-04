from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle

def home(request):
    context = {
        'vehicles': Vehicle.objects.all()
    }
    return render(request, 'home/home.html', context)
    
def about(request):
    return render(request, 'home/about.html')