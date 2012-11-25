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
    url = models.URLField(verbose_name='URL', blank=True,
            default=None, null=True,
            help_text='URL to link to. Leave blank if uploading a file.')
    file = models.FileField(upload_to='links', blank=True,
            null=True, default=None, max_length=500,
            help_text='A file to be uploaded and linked to instead ' \
            + 'of the URL.')
    category = models.ForeignKey(Category, null=True, related_name='links')
    description = models.TextField(null=True,
            help_text='Description of the link or file contents')
    visits = models.IntegerField(default=0, editable=False,
            help_text='Number of visitors who clicked on this link')

    def get_absolute_url(self):
        return reverse('track_link', args=(self.id,))

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.file:
            self.url = self.file.url

        return super(Link, self).save(*args, **kwargs)
