from django.conf.urls import patterns, url
from django.conf import settings


urlpatterns = patterns('pylinks.main.views',
    url(r'^$', 'index', name='index'),
)
