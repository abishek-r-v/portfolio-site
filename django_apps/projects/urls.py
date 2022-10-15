from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_projects, name="disp_projects"),
]
