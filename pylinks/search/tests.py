from django.core.management import call_command
from django.core.urlresolvers import reverse
from django.test import TestCase

from pylinks.links.models import Link
from pylinks.links import search_indexes

import haystack

class SearchViewTests(TestCase):
    def setUp(self):
        haystack.connections.reload('default')
        haystack.connections['default'].get_backend().clear()

    def test_search(self):
        Link(title='GitHub', url='https://github.com')
        link = Link(title='Google', url='https://www.google.ca')
        link.save()

        response = self.client.get(reverse('haystack_search') + '?q=Google')
        self.assertEqual(map(lambda o: o.object, response.context['page'].object_list), [link])
