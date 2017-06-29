from django.conf.urls import url
from pylinks.search.views import SearchView

urlpatterns = (
    url(r'^$', SearchView(), name='haystack_search'),
)
