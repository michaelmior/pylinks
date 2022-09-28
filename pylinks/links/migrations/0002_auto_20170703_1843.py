import os

from django.db import migrations, models

if not os.environ.get("UPLOADCARE_DISABLED", False):
    from pylinks.links.utils import LinkFileField
else:
    from django.db.models import FileField as LinkFileField


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="file",
            field=LinkFileField(
                default=None,
                max_length=500,
                null=True,
                help_text=b"A file to be uploaded and linked to instead of the URL.",
                blank=True,
            ),
            preserve_default=True,
        ),
    ]
