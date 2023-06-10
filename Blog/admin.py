from django.contrib import admin

from .models import Blog, Tag

admin.site.register(Blog)
admin.site.register(Tag)
