from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Story
from .tasks import preprocess


@receiver(post_save, sender=Story)
def preprocess_story_media(sender, instance, created, **kwargs):
    if instance.image or instance.video:
        preprocess(instance.id)