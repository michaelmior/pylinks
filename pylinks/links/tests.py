from django.test import Client, TestCase

from .models import Category, Link

class CategoryModelTests(TestCase):

    def test_category_sort(self):
        Category(title='Test 2', slug='test2').save()
        Category(title='Test 1', slug='test1').save()

        self.assertEqual(['Test 1', 'Test 2'], map(str, Category.objects.all()))

class LinkModelTests(TestCase):
    def setUp(self):
        self.url = 'https://github.com/'
        self.link = Link(title='GitHub', url=self.url)

    def test_track_link(self):
        self.assertEqual(self.link.get_absolute_url(), self.url)
        self.link.save()
        self.assertEqual(self.link.visits, 0)
        self.assertEqual(self.link.get_absolute_url(), '/links/go/%d/' % self.link.id)

    def test_link_title(self):
        self.assertEqual(str(self.link), 'GitHub')

    def test_increment_visits(self):
        self.link.save()
        client = Client()
        response = client.get('/links/go/%d/' % self.link.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], self.link.url)
        self.assertEqual(Link.objects.get(pk=self.link.id).visits, 1)
