from django import forms
from home.models import Commit_visit
from . import models


class CommitForm(forms.ModelForm):
    class Meta:
        model = Commit_visit
        fields = ('first_name', 'last_name', 'email', 'text_input',)
    