from django.db import models
from django.core.urlresolvers import reverse
from pylinks.main.models import DatedModel


class Category(DatedModel):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(help_text='Text for the URL')
    description = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('category_links', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Link(DatedModel):
    title = models.CharField(max_length=200)
    url = models.URLField(verbose_name='URL')
    category = models.ForeignKey(Category, null=True, related_name='links')
    description = models.TextField(null=True)

    def get_absolute_url(self):
        return self.url

    def __unicode__(self):
        return self.title
