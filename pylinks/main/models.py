from django.contrib.sites.models import Site
from django.db import models


class DatedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        get_latest_by = 'updated_time'


class SiteInfo(models.Model):
    site = models.OneToOneField(Site, primary_key=True,
                                on_delete=models.CASCADE)
    description = models.TextField(null=True)

    def __self__(self):
        return str(self.site)

    class Meta:
        verbose_name_plural = 'site info'

    def save(self, *args, **kwargs):
        # Ensure the site cache is cleared so the new
        # info will be loaded next time
        rc = super().save(*args, **kwargs)
        Site.objects.clear_cache()
        return rc
