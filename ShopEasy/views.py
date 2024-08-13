from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    services = models.Services.objects.all()
    aboutme = models.AboutMe.objects.all()
    context = {
        'service':services,
        'aboutus':aboutme
    }
    return render(request, 'index.html', context)
