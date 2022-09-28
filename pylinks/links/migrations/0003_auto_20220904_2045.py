# Generated by Django 2.2.20 on 2022-09-04 20:45

from django.db import migrations, models

import pylinks.links.utils


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0002_auto_20170703_1843"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(help_text="Text for the URL"),
        ),
        migrations.AlterField(
            model_name="link",
            name="description",
            field=models.TextField(
                help_text="Description of the link or file contents", null=True
            ),
        ),
        migrations.AlterField(
            model_name="link",
            name="file",
            field=pylinks.links.utils.LinkFileField(
                blank=True,
                default=None,
                help_text="A file to be uploaded and linked to instead of the URL.",
                max_length=500,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="link",
            name="url",
            field=models.URLField(
                blank=True,
                default=None,
                help_text="URL to link to. Leave blank if uploading a file.",
                null=True,
                verbose_name="URL",
            ),
        ),
        migrations.AlterField(
            model_name="link",
            name="visits",
            field=models.IntegerField(
                default=0,
                editable=False,
                help_text="Number of visitors who clicked on this link",
            ),
        ),
    ]
