from django.conf.urls import patterns, url
from pylinks.feeds import feeds


urlpatterns = patterns('',
    url(r'^category/(?P<slug>.*)/', feeds.CategoryFeed()),
    url(r'^recent/', feeds.RecentFeed()),
    url(r'^popular/', feeds.PopularFeed()),
)
