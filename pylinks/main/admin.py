from django.contrib import admin

from pylinks.main import models


class ModelAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"


class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ("site", "description")


admin.site.register(models.SiteInfo, SiteInfoAdmin)
