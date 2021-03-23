from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Story(models.Model):

    def upload_image_location(instance, filename):
        return "images/storyimage/%s/%s" % (instance.slug, filename)

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
    video = models.FileField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grapher.email

