from django.contrib import admin

from pylinks.links import models
from pylinks.main.admin import ModelAdmin


class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    search_fields = ('title',)

admin.site.register(models.Category, CategoryAdmin)


class LinkAdmin(ModelAdmin):
    class Media:
        js = ('js/uploadcare.js',)

    list_display = ('title', 'url')
    list_filter = ('categories',)
    readonly_fields = ('visits',)
    search_fields = ('title',)

admin.site.register(models.Link, LinkAdmin)
