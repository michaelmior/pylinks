from django.db import models


class DatedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        get_latest_by = 'updated_time'
