from django.shortcuts import render,redirect
from home.data import projects
from home.section_data import section_data

from home.forms import CommitForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CommitForm(request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('\\')

        return render(
            request,
            'global\index.html',
            context
        )
     
    context = {
        'form': CommitForm(),
        'section_data': section_data,
        'projects': projects,
    }

    return render(request,
                  'global\index.html',
                  context,
                  )
    
    