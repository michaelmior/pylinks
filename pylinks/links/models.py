import os

from django.db import models
from django.urls import reverse
from pylinks.main.models import DatedModel

if not os.environ.get('UPLOADCARE_DISABLED', False):
    from pylinks.links.utils import LinkFileField
else:
    from django.db.models import FileField as LinkFileField


class Category(DatedModel):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(help_text='Text for the URL')
    description = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('category_links', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'categories'


class Link(DatedModel):
    title = models.CharField(max_length=200)
    url = models.URLField(verbose_name='URL', blank=True,
            default=None, null=True,
            help_text='URL to link to. Leave blank if uploading a file.')
    file = LinkFileField(blank=True, null=True, default=None, max_length=500,
            help_text='A file to be uploaded and linked to instead ' \
            + 'of the URL.', upload_to='uploads/')
    categories = models.ManyToManyField(Category, related_name='links')
    description = models.TextField(null=True,
            help_text='Description of the link or file contents')
    visits = models.IntegerField(default=0, editable=False,
            help_text='Number of visitors who clicked on this link')

    def get_absolute_url(self):
        if self.id:
            return reverse('track_link', args=(self.id,))
        elif self.file:
            return self.file.cdn_url
        elif self.url:
            return self.url
        else:
            return None

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<Link: {}>'.format(self.title)

    class Meta:
        ordering = ('title',)

    def save(self, *args, **kwargs):
        if self.file:
            self.url = self.file.cdn_url

        return super(Link, self).save(*args, **kwargs)
