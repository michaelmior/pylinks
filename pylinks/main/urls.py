from django.conf import settings
from django.conf.urls import url

from pylinks.main import views

if getattr(settings, 'PYLINKS_HOME', None) == 'alpha':
    index_url = url(r'^$', views.alpha_index, name='index')
else:
    index_url = url(r'^$', views.category_index, name='index')


urlpatterns = (index_url,)
