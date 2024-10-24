from django.contrib import admin
from .models import Projects
from .models import Engineer

# Register your models here.

admin.site.register(Projects)
admin.site.register(Engineer)

