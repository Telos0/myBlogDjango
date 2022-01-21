from django.shortcuts import render
from blog.models import RunningServices

# Create your views here.

def landing(request):
    running_services = RunningServices.objects.filter(runningYN=1)
    return render(request, 'single_pages/landing.html', { 'running_services' : running_services })

def about_me(request):
    return render(request, 'single_pages/about_me.html')