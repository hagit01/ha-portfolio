from django.shortcuts import render
from .models import Project, Skill
# Create your views here.


def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.filter(body='')
    return render(request, 'base/home.html', {'projects': projects, 'skills': skills})