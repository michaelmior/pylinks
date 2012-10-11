from django.conf.urls import url, patterns
from pylinks.search.views import SearchView

urlpatterns = patterns('',
    url(r'^$', SearchView(), name='haystack_search')
)
