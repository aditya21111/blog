from django.contrib import admin

# Register your models here.
from .models import Contact ,Profile

admin.site.register(Contact)
admin.site.register(Profile)
