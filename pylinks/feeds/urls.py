from django.conf.urls import url

from pylinks.feeds import feeds

urlpatterns = (
    url(r'^category/(?P<slug>.*)/', feeds.CategoryFeed(),
      name='feed_category'),
    url(r'^recent/', feeds.RecentFeed(),
      name='feed_recent'),
    url(r'^popular/', feeds.PopularFeed(),
      name='feed_popular'),
)
