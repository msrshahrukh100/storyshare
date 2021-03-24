from rest_framework import serializers
from .models import Story
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class StorySerializer(serializers.ModelSerializer):
    grapher_username = serializers.CharField(source='grapher.username')

    class Meta:
        model = Story
        fields = ("grapher_username", "image", "name", "text", "preprocessing_done")
        read_only_fields = ("height_field", "width_field")
    
    def create(self, validated_data):
        print(validated_data)
        grapher = get_object_or_404(User, username=validated_data.get("grapher", {}).get("username"))
        validated_data["grapher"] = grapher
        return Story.objects.create(**validated_data)
        