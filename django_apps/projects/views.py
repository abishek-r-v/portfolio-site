from django.shortcuts import render
from . import models


# Create your views here.
def display_projects(request):
    projects = models.Project.objects.order_by('-entry_date')
    return render(
        request=request,
        template_name='projects/disp_projects.html',
        context={'projects': projects}
    )