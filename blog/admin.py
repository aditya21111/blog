from django.contrib import admin

# Register your models here.
from .models import Blogpost,comments


class commentAdmin(admin.ModelAdmin):
    list_display = ('short_comment', 'user',"timestamp","is_approved",)

admin.site.register(comments,commentAdmin)

class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', "writer","pub_date",)

admin.site.register(Blogpost,BlogpostAdmin)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinymceinject.js',)