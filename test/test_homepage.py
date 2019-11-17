from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User
from datetime import datetime
from blog_app.models import Blog


class HomepageTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        self.user = User.objects.create_user(username='phodal',
                                             email='h@phodal.com',
                                             password='phodal')
        super(HomepageTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(HomepageTestCase, self).tearDown()

    def test_can_visit_homepage(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertIn("Growth Studio - Enjoy Create & Share",
                      self.selenium.title)

    def test_should_goto_blog_page_from_homepage(self):
        Blog.objects.create(title='hello',
                            author=self.user,
                            slug='this_is_a_test',
                            body='This is blog detail',
                            posted=datetime.now)
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element_by_link_text('博客').click()

        self.assertIn("This is blog detail", self.selenium.page_source)
