from django.urls import re_path

from pylinks.feeds import feeds

urlpatterns = (
    re_path(r"^category/(?P<slug>.*)/", feeds.CategoryFeed(), name="feed_category"),
    re_path(r"^recent/", feeds.RecentFeed(), name="feed_recent"),
    re_path(r"^popular/", feeds.PopularFeed(), name="feed_popular"),
)
