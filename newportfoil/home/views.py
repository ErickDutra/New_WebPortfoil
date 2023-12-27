from django.shortcuts import render
from home.data import projects
from home.section_data import section_data

from home.forms import CommitForm


# Create your views here.
def index(request):
    
    if request.method == 'POST':
        ...

    context = {
        'form': CommitForm(),
        'section_data': section_data,
        'projects': projects,
    }
    
    return render(request,
                  'global\index.html',
                  context,
                  )
