from django.urls import path
from .views import StoryListCreate


urlpatterns = [
    path("story/", StoryListCreate.as_view(), name="story_list_create"),
]
