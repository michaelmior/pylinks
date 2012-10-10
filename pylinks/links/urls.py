from django.conf.urls import patterns, url
from pylinks.links import views

urlpatterns = patterns('pylinks.links.views',
    url(r'^category/(?P<slug>[A-z0-9_\-]*)/(?:(?P<page>\d+)/)?$',
        views.CategoryListView.as_view(),
        name='category_links'),

    url(r'^recent/(?:(?P<page>\d+)/)?$',
        views.RecentListView.as_view(),
        name='recent_links'),

    url(r'^popular/(?:(?P<page>\d+)/)?$',
        views.PopularListView.as_view(),
        name='popular_links'),

    url(r'^go/(?P<link_id>\d+)/$', 'track_link', name='track_link'),
)
