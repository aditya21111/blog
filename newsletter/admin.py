from django.contrib import admin
from newsletter.models import Newsletter

# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at',)

admin.site.register(Newsletter,NewsletterAdmin)

