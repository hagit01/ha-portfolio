from django.shortcuts import render
from .models import Project, Skill
from .forms import ProjectForm
# Create your views here.


def home(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')
    context = {'projects': projects, 'skills': skills, 'detailedSkills':detailedSkills}
    return render(request, 'base/home.html', context)


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'base/project.html', context)


def addProject(request):
    context = {}
    return render(request, 'base/project_form.html', context)