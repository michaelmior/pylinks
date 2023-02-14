from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_time", models.DateTimeField(auto_now=True, null=True)),
                ("title", models.CharField(unique=True, max_length=200)),
                ("slug", models.SlugField(help_text=b"Text for the URL")),
                ("description", models.TextField(null=True)),
            ],
            options={
                "ordering": ("title",),
                "verbose_name_plural": "categories",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_time", models.DateTimeField(auto_now=True, null=True)),
                ("title", models.CharField(max_length=200)),
                (
                    "url",
                    models.URLField(
                        default=None,
                        blank=True,
                        help_text=b"URL to link to. Leave blank if uploading a file.",
                        null=True,
                        verbose_name=b"URL",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        default=None,
                        upload_to=b"uploads/",
                        max_length=500,
                        blank=True,
                        help_text=b"A file to be uploaded and linked to instead of the URL.",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text=b"Description of the link or file contents", null=True
                    ),
                ),
                (
                    "visits",
                    models.IntegerField(
                        default=0,
                        help_text=b"Number of visitors who clicked on this link",
                        editable=False,
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(related_name="links", to="links.Category"),
                ),
            ],
            options={
                "ordering": ("title",),
            },
            bases=(models.Model,),
        ),
    ]
