# posts/tests.py
from django.test import TestCase

from .models import Post


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_modelContent(self):
        self.assertEqual(self.post.text, "This is a test!")
