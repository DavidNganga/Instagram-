from django.test import TestCase
from .models import Profile,Image,Comment
from django.contrib.auth.models import User
# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method to run before each test case.
    def setUp(self):
        user=User(username='viking',email="ngashiedavid@gmail.com",password="alforgett")
        self.david= Profile(name = 'David', bio ='whatever', profile_photo='example-01.png',user=user )

    def test_instance(self):
        self.assertTrue(isinstance(self.david,Profile))
#
class ImageTestClass(TestCase):

    def setUp(self):
        profile=Profile(name = 'David', bio ='whatever', profile_photo='example-01.png',user=user )
        self.david= Image(name='xy',caption='xz',image='example-01.png')

    def test_instance(self):
        self.assertTrue(isinstance(self.david,Profile))
class CommentTestClass(TestCase):
    def setUp(self):
        self.david= Comment(name="David", email="ngashiedavid@gmail.com")
