from django.contrib import admin

# Register your models here.
from .models import Blogpost,comments
admin.site.register((Blogpost,comments))

