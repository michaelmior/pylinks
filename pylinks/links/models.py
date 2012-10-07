from django.db import models
from pylinks.main.models import DatedModel


class Category(DatedModel):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(help_text='Text for the URL')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Link(DatedModel):
    title = models.CharField(max_length=200)
    url = models.URLField(verbose_name='URL')
    category = models.ForeignKey(Category, null=True, related_name='links')

    def __unicode__(self):
        return self.title
