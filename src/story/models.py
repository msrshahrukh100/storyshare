from django.db import models
from django.contrib.auth.models import User
from video_encoding.fields import VideoField
from django.contrib.contenttypes.fields import GenericRelation
from video_encoding.models import Format

# Create your models here.



class Story(models.Model):

    def upload_image_location(instance, filename):
        return "images/storyimage/%s" % filename
    
    def upload_image_location_resized(instance, filename):
        return "images/storyimage/resized/%s" % filename

    grapher = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=upload_image_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field",
    )
    height_field = models.IntegerField(null=True, blank=True, default=0)
    width_field = models.IntegerField(null=True, blank=True, default=0)
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    duration = models.FloatField(editable=False, null=True)
    video = VideoField(duration_field='duration', null=True, blank=True)
    format_set = GenericRelation(Format)
    preprocessing_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
