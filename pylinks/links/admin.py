from django.contrib import admin
from pylinks.links import models


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Category, CategoryAdmin)


class LinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Link, LinkAdmin)
