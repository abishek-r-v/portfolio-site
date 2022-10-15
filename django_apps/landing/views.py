from django.shortcuts import render
from . import models


# Create your views here.
def render_home(request):
    about_me = models.AboutMeContent.objects.order_by('paragraph_id')
    return render(
        request=request,
        template_name='landing/home.html',
        context={'about_me': about_me }
    )
