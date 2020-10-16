from django.conf.urls import url

from pylinks.links import views

urlpatterns = (
    url(r'^alpha/(?P<letter>[A-Z])/(?:(?P<page>\d+)/)?$',
        views.AlphaListView.as_view(),
        name='category_alpha'),

    url(r'^category/(?P<slug>[A-z0-9_\-]*)/(?:(?P<page>\d+)/)?$',
        views.CategoryListView.as_view(),
        name='category_links'),

    url(r'^recent/(?:(?P<page>\d+)/)?$',
        views.RecentListView.as_view(),
        name='recent_links'),

    url(r'^popular/(?:(?P<page>\d+)/)?$',
        views.PopularListView.as_view(),
        name='popular_links'),

    url(r'^go/(?P<link_id>\d+)/$', views.track_link, name='track_link'),
)
