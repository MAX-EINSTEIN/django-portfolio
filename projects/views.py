from django.shortcuts import render
from .models import Project

# Create your views here.
def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})