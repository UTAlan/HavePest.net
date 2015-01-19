from django.contrib import admin
from home.models import Content

class ContentAdmin(admin.ModelAdmin):
    fields = ('title', 'content')

admin.site.register(Content, ContentAdmin)
