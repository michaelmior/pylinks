from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('site', models.OneToOneField(primary_key=True, serialize=False, to='sites.Site', on_delete=models.CASCADE)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'site info',
            },
            bases=(models.Model,),
        ),
    ]
