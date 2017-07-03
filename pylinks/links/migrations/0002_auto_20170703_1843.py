# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pylinks.links.utils


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='file',
            field=pylinks.links.utils.LinkFileField(default=None, max_length=500, null=True, help_text=b'A file to be uploaded and linked to instead of the URL.', blank=True),
            preserve_default=True,
        ),
    ]
