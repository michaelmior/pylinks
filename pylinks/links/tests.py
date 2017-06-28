from django.test import TestCase

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
