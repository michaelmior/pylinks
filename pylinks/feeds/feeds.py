import re

from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from pylinks.links.models import Category, Link


control_re = re.compile(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]')


class BaseFeed(Feed):
    def item_guid(self, item):
        return str(item.pk)

    def item_description(self, item):
        return control_re.sub('', item.description)

    def item_pubdate(self, item):
        return item.created_time

    def item_categories(self, item):
        return [category.title for category in item.categories.all()]


class CategoryFeed(BaseFeed):

    def get_object(self, request, slug):
        return get_object_or_404(Category, slug=slug)

    def title(self, obj):
        return 'Links for ' + control_re.sub('', obj.title)

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return control_re.sub('', obj.description)

    def items(self, obj):
        return obj.links.order_by('-created_time')[:30]


class RecentFeed(BaseFeed):

    def title(self):
        return 'Recent links'

    def link(self):
        return reverse('recent_links')

    def items(self):
        return Link.objects.order_by('-created_time')[:30]


class PopularFeed(BaseFeed):

    def title(self):
        return 'Popular links'

    def link(self):
        return reverse('popular_links')

    def items(self):
        return Link.objects.order_by('-visits')[:30]
