from django.shortcuts import render
from .models import Project, Skill
# Create your views here.


def home(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.filter(body='')
    skills = Skill.objects.filter(body='')
    context = {'projects': projects, 'skills': skills}
    return render(request, 'base/home.html', )