from django.contrib import admin
from pylinks.main.admin import ModelAdmin
from pylinks.links import models


class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    search_fields = ('title',)

admin.site.register(models.Category, CategoryAdmin)


class LinkAdmin(ModelAdmin):
    list_display = ('title', 'url')
    list_filter = ('category__title',)
    search_fields = ('title',)

admin.site.register(models.Link, LinkAdmin)
