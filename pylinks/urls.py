from django.conf.urls import patterns, include, url


from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

admin.autodiscover()
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pylinks.views.home', name='home'),
    # url(r'^pylinks/', include('pylinks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
