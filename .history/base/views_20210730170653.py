from django.shortcuts import render
from .models import Project, Skill
# Create your views here.


def home(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.filter(body_not='')
    skills = Skill.objects.filter(body='')
    context = {'projects': projects, 'skills': skills, 'detailedSkills':detailedSkills}
    return render(request, 'base/home.html', context)