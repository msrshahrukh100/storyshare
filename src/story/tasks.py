from background_task import background
from .models import Story
from PIL import Image


def preprocess_image(story):
    to_resize = Image.open(story.image.path)
    if to_resize.width > 1200 or to_resize.height > 600:
        output_size = (1200, 600)
        to_resize.thumbnail(output_size)
        to_resize.save(story.image.path)
        story.preprocessing_done = True
        story.height_field = to_resize.height
        story.width_field = to_resize.width
        story.save()


@background(schedule=5)
def preprocess(story_id):
    story = Story.objects.get(id=story_id)
    if story.image:
        preprocess_image(story)
    

