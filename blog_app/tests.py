from datetime import datetime

from django.contrib.auth.models import User
from django.urls import resolve
from django.test import TestCase

from blog_app.models import Blog
from blog_app.views import blog_list

# Create your tests here.


class BlogpostListTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='phodal',
                                             email='h@phodal.com',
                                             password='phodal')

    def test_blog_list_page(self):
        Blog.objects.create(title='hello',
                            author=self.user,
                            slug='this_is_a_test',
                            body='This is a blog',
                            posted=datetime.now)
        response = self.client.get('/blog/')
        self.assertIn(b'This is a blog', response.content)

    def test_not_found_blog(self):
        response = self.client.get('/blog/this_not_a_blog.html')
        self.assertEqual(404, response.status_code)
