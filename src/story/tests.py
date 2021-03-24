from django.test import TestCase
from story.models import Story
from PIL import Image
import tempfile
from rest_framework import status
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from .views import StoryListCreate

factory = APIRequestFactory()


class StoryTestCase(TestCase):
    def setUp(self):
        pass

    def test_story_create(self):
        image = Image.new('RGB', (1000, 1000))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)

        # Send data
        with open(tmp_file.name, 'rb') as data:
            request = factory.post(
                reverse('story_list_create'),
                {
                    'name': 'Test name',
                    'text': 'A text to test',
                    'grapher': 1,
                    'image': data
                },
                format='multipart')
            view = StoryListCreate.as_view()
            response = view(request)
            print(dir(response))
            print(response.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)      
        self.assertEqual(True, True)
