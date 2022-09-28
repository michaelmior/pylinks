from django.conf import settings
from django.urls import re_path

from pylinks.main import views

if getattr(settings, "PYLINKS_HOME", None) == "alpha":
    index_url = re_path(r"^$", views.alpha_index, name="index")
else:
    index_url = re_path(r"^$", views.category_index, name="index")


urlpatterns = (index_url,)
