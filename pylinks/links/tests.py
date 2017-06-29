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
        self.assertEqual(self.link.get_absolute_url(),
            '/links/go/%d/' % self.link.id)

    def test_link_title(self):
        self.assertEqual(str(self.link), 'GitHub')

    def test_increment_visits(self):
        self.link.save()
        response = self.client.get('/links/go/%d/' % self.link.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], self.link.url)
        self.assertEqual(Link.objects.get(pk=self.link.id).visits, 1)

class ListViewTests(TestCase):
    def setUp(self):
        ca = Category(title='A', slug='a')
        ca.save()
        cb = Category(title='B', slug='b')
        cb.save()

        link = Link(title='Google', url='https://www.google.ca', visits=1)
        link.save()
        ca.links.add(link)

        link = Link(title='GitHub', url='https://github.com', visits=2)
        link.save()
        ca.links.add(link)

        link = Link(title='UW', url='https://uwaterloo.ca', visits=3)
        link.save()
        cb.links.add(link)

class CategoryListViewTests(ListViewTests):
    def test_category_list(self):
        response = self.client.get('/links/category/a/')
        self.assertQuerysetEqual(response.context['links'], [
            '<Link: GitHub>',
            '<Link: Google>'
        ])

class PopularListViewTests(ListViewTests):
    def test_popular_list(self):
        response = self.client.get('/links/popular/')
        self.assertQuerysetEqual(response.context['links'], [
            '<Link: UW>',
            '<Link: GitHub>',
            '<Link: Google>'
        ])

class RecentListViewTests(ListViewTests):
    def test_recent_list(self):
        response = self.client.get('/links/recent/')
        self.assertQuerysetEqual(response.context['links'], [
            '<Link: UW>',
            '<Link: GitHub>',
            '<Link: Google>'
        ])
