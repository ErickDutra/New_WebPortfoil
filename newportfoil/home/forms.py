from django import forms
from home.models import Commit_visit


class CommitForm(forms.ModelForm):
    class Meta:
        model = Commit_visit
        fields = ('first_name', 'last_name', 'email', 'text_input',)
    
        widgets = {
            'first_name': forms.TextInput(
               attrs= {'placeholder' : 'Primeiro nome',}
            ),
            
            'last_name': forms.TextInput(
               attrs= {'placeholder' : 'Ultimo nome',}
            ),
            'email': forms.TextInput(
               attrs= {'placeholder' : 'email@email.com',}
            ),
            'text_input': forms.Textarea(
               attrs= {'placeholder' : 'Deixe uma mensagem aqui... ',}
            )
        }