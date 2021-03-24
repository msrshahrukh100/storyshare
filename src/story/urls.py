from django.urls import path
from .views import StoryListCreate, StoryDetailUpdateDelete


urlpatterns = [
    path("story/", StoryListCreate.as_view(), name="story_list_create"),
    path("story/<int:id>", StoryDetailUpdateDelete.as_view(), name="story_retrive_delete_update"),
]
