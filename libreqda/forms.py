from django import forms
from django.contrib.auth.models import User

from libreqda.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('owner', 'version', 'creation_date', 'modified_date')


class AddUserToProjectForm(forms.Form):
    users = forms.ModelMultipleChoiceField(
                        queryset=User.objects.all(),
                        label='Usuarios')