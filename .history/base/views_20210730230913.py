from django.shortcuts import render
from .models import Project, Skill
# Create your views here.


def home(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')
    context = {'projects': projects, 'skills': skills, 'detailedSkills':detailedSkills}
    return render(request, 'base/home.html', context)


def projectPage(request, pk):
    project =
    context = {}
    return render(request, 'base/project.html', context)