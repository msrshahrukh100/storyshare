from django.shortcuts import render
from rest_framework import generics
from .models import Story
from .serializers import StorySerializer
# Create your views here.

class StoryListCreate(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    serializer_class = StorySerializer
    queryset = Story.objects.all()

    
