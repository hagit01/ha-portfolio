from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    self.