from django.conf.urls import patterns, url
from django.conf import settings

if getattr(settings, 'PYLINKS_HOME', None) == 'alpha':
    index_url = url(r'^$', 'alpha_index', name='index')
else:
    index_url = url(r'^$', 'category_index', name='index')


urlpatterns = patterns('pylinks.main.views', index_url)
