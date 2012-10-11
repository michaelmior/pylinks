from django.conf.urls import patterns, url


urlpatterns = patterns('pylinks.main.views',
    url(r'^$', 'index', name='index'),
)
