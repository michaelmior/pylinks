from django.conf.urls import patterns, include, url


from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

admin.autodiscover()
#admin.site.unregister(User)
#admin.site.unregister(Group)
#admin.site.unregister(Site)

urlpatterns = patterns('',
    url(r'^feed/', include('pylinks.feeds.urls')),
    url(r'^links/', include('pylinks.links.urls')),
    url(r'^search/', include('pylinks.search.urls')),
    url(r'^', include('pylinks.main.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)
