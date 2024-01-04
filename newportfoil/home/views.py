from django.shortcuts import render,redirect
from home.data import projects
from home.section_data import section_data
from django.contrib import messages
from home.forms import CommitForm


# Create your views here.
def index(request):
    
    #method post
    if request.method == 'POST':
        form = CommitForm(request.POST)

        
        context = {
            'form': form,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Obrigado pela mensagem')
            return redirect('/')

        return render(
            request,
            'home/index.html',
            context,
            
        )

    #view html
    context = {
        'form': CommitForm(),
        'section_data': section_data,
        'projects': projects,
            }
    return render(
        request,
        'home/index.html',
        context,
        )
