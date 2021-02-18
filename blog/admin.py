from django.contrib import admin

# Register your models here.
from .models import Blogpost,comments
admin.site.register(Blogpost,comments)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('tinymceinject.js')