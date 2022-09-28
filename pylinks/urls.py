from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
from django.urls import include, re_path

admin.autodiscover()
#admin.site.unregister(User)
#admin.site.unregister(Group)
#admin.site.unregister(Site)

urlpatterns = (
    re_path(r'^feed/', include('pylinks.feeds.urls')),
    re_path(r'^links/', include('pylinks.links.urls')),
    re_path(r'^search/', include('pylinks.search.urls')),
    re_path(r'^', include('pylinks.main.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^grappelli/', include('grappelli.urls')),
)
