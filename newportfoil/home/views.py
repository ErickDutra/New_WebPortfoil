from django.shortcuts import render

from home.data import projects
from home.section_data import section_data


# Create your views here.
def index(request):
    print()
    context = {
        'section_data': section_data,
        'projects': projects,
    }
    return render(request,
                  'global\index.html',
                  context,
                  )