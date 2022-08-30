from django.test import TestCase

from django.test import SimpleTestCase

from django.urls import reverse

# Create your tests here.
from .models import Post

class PostTests(TestCase): 
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
    def test_model_content(self): 
        self.assertEqual(self.post.text, "This is a test!")