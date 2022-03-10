from django.shortcuts import render
from blog.models import RunningServices
from .models import Contents

# Create your views here.

def landing(request):
    running_services = RunningServices.objects.all()
    return render(request, 'single_pages/landing.html', { 'running_services' : running_services })

def about_me(request):
    contents_WorkExperience = Contents.objects.filter(contentsid='Work Experience').filter(useYN='True')
    contents_Education = Contents.objects.filter(contentsid='Education').filter(useYN='True')
    contents_Certificate = Contents.objects.filter(contentsid='Certificate').filter(useYN='True')
    return render(request, 'single_pages/about_me.html', {'contents_WorkExperience' : contents_WorkExperience,
                                                          'contents_Education' : contents_Education,
                                                          'contents_Certificate' : contents_Certificate })