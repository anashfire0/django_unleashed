from django.contrib import admin
from .models import StartUp, Tag, NewsLink
# Register your models here.

admin.site.register(StartUp)
admin.site.register(Tag)
admin.site.register(NewsLink)