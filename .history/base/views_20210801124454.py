from django.shortcuts import render, redirect
from .models import Project, Skill, Message, Endorsement
from .forms import ProjectForm, MessageForm, SkillForm, EndorsementForm, Form 
from django.contrib import messages
# Create your views here.


def home(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')
    endorsements = Endorsement.objects.filter(approved=True)
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was successfully sent!.')
    context = {'projects': projects, 'skills': skills, 'detailedSkills':detailedSkills, 'form': form, 'endorsements': endorsements}
    return render(request, 'base/home.html', context)


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    count = project.comment_set.count()

    comments = project.comment_set.all()
    context = {'project': project, 'count': count, 'comments': comments}

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


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unreadCount = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unreadCount': unreadCount}
    return render(request, 'base/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'base/message.html', context)


def addSkill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        form.save()
        messages.success(request, 'Your skill was successfully added.')
        return redirect("base:home")
    context = {'form': form}

    return render(request, 'base/skill_form.html', context)



def addEndorsement(request):
    form = EndorsementForm()
    if request.method == "POST":
        form = EndorsementForm(request.POST)
        form.save()
        messages.success(request, 'Thank you, your endorsement was successfully added!.')
        return redirect('base:home')
    context = {'form': form}
    return render(request, 'base/endorsement_form.html', context)


