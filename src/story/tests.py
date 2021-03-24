from django.test import TestCase
from story.models import Story
from PIL import Image
import tempfile
from rest_framework import status
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from .views import StoryListCreate
from django.contrib.auth.models import User
from PIL import Image
from urllib import request as ulreq

factory = APIRequestFactory()
 
def getsizes(uri):
    file = ulreq.urlopen(uri)
    f = Image.open(file)
    return (f.height, f.width)

class StoryTestCase(TestCase):
    def setUp(self):
        self.response_data = None
        self.user = User.objects.create_user('test', 'test@test.com', 'testpassword')

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
                    'grapher_username': self.user.username,
                    'image': data
                },
                format='multipart')
            view = StoryListCreate.as_view()
            response = view(request)
            # print(getsizes(response.data.get("image")))
            # print(response.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # def test_resized_image(self):
    #     to_test = Image.open(self.response_data.get("image"))
    #     print(to_test.width, to_test.height)


