from django.db import models
from pylinks.main.models import DatedModel


class Category(DatedModel):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'


class Link(DatedModel):
    title = models.CharField(max_length=200)
    url = models.URLField()
    category = models.ForeignKey(Category, null=True)
