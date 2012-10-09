from django.conf.urls import patterns, url
from pylinks.links import views

urlpatterns = patterns('',
    url(r'^category/(?P<slug>[A-z0-9_\-]*)/(?:(?P<page>\d+)/)?$',
        views.CategoryListView.as_view(),
        name='category_links'),

    url(r'^recent/(?:(?P<page>\d+)/)?$',
        views.RecentListView.as_view(),
        name='recent_links'),
)
