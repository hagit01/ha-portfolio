from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Enter username...'}
    )
    self.fields['password1'].widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Enter'}
    )