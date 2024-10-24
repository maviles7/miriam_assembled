from django.shortcuts import render
from .models import Projects
from .models import Engineer

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    engineer = Engineer.objects.all
    return render(request, 'about.html', {'engineer': engineer })

def projects_index(request):
    projects = Projects.objects.all()
    return render(request, 'projects/project_index.html', {'projects': projects}) 