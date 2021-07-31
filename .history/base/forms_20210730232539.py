from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    model = Project
    fields = '__all__'
    pass