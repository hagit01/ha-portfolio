from django.shortcuts import render, redirect
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
    form = ProjectForm

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def addProject(request):
    form = Project.object.get(id=pk)

    
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)