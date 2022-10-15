from django.contrib import admin
from .models import TechStack, Package, Framework, Project,Image

# Register your models here.
admin.site.register(TechStack)
admin.site.register(Package)
admin.site.register(Framework)
admin.site.register(Project)
admin.site.register(Image)
