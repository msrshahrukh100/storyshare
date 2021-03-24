from django.contrib import admin
from .models import Story
from video_encoding.admin import FormatInline

# Register your models here.


class StoryAdmin(admin.ModelAdmin):
   inlines = (FormatInline,)
   list_dispaly = ('name', 'duration')

admin.site.register(Story, StoryAdmin)