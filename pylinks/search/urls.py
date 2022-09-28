from django.urls import re_path

from pylinks.search.views import SearchView

urlpatterns = (re_path(r"^$", SearchView(), name="haystack_search"),)
