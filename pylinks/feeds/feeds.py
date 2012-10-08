from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from pylinks.links.models import Category, Link


class BaseFeed(Feed):
    def item_guid(self, item):
        return unicode(item.pk)

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return item.created_time

    def item_categories(self, item):
        category = item.category
        return (category.title,) if category else ()


class CategoryFeed(BaseFeed):

    def get_object(self, request, slug):
        return get_object_or_404(Category, slug=slug)

    def title(self, obj):
        return 'Links for ' + obj.title

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return obj.description

    def items(self, obj):
        return obj.links.order_by('-created_time')[:30]


class RecentFeed(BaseFeed):

    def title(self):
        return 'Recent links'

    def link(self):
        # TODO Add recent links page
        return u''

    def items(self):
        return Link.objects.order_by('-created_time')[:30]
