from django.urls import re_path

from pylinks.links import views

urlpatterns = (
    re_path(
        r"^alpha/(?P<letter>[A-Z])/(?:(?P<page>\d+)/)?$",
        views.AlphaListView.as_view(),
        name="category_alpha",
    ),
    re_path(
        r"^category/(?P<slug>[A-z0-9_\-]*)/(?:(?P<page>\d+)/)?$",
        views.CategoryListView.as_view(),
        name="category_links",
    ),
    re_path(
        r"^recent/(?:(?P<page>\d+)/)?$",
        views.RecentListView.as_view(),
        name="recent_links",
    ),
    re_path(
        r"^popular/(?:(?P<page>\d+)/)?$",
        views.PopularListView.as_view(),
        name="popular_links",
    ),
    re_path(r"^go/(?P<link_id>\d+)/$", views.track_link, name="track_link"),
)
