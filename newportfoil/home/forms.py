from django import forms
from home.models import Commit_visit
from django.core.exceptions import ValidationError



class CommitForm(forms.ModelForm):
   
   class Meta:
      model = Commit_visit
      fields = ('first_name', 'last_name', 'email', 'text_input',)
      
      widgets ={
                  'first_name': forms.TextInput(
                     attrs= {'placeholder' : 'Primeiro nome',}
                  ),
                  'last_name': forms.TextInput(
                     attrs= {'placeholder' : 'Último nome',}
                  ),
                  'email': forms.TextInput(
                     attrs= {'placeholder' : 'email@email.com',}
                  ),
                  'text_input': forms.Textarea(
                     attrs= {'placeholder' : 'Deixe uma mensagem aqui... ',}
                  )
               }
      
   def clean_email(self):
      email = self.cleaned_data.get('email')

      if Commit_visit.objects.filter(email=email).exists():
         self.add_error(
               'email',
               ValidationError('Já existe mensagem com este e-mail', code='invalid')
         )
      
      return email
         
   
   def clean(self):
      cleaned_data = self.cleaned_data
      first_name = cleaned_data.get('first_name')
      last_name = cleaned_data.get('last_name')
      
      if last_name == first_name:
         self.add_error(
            'last_name',
            ValidationError(
               'último nome, não pode ser igual ao primeiro.',
               code='invalid'
            )
         )
         
      return super().clean()
   
   