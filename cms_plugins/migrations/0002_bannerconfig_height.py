# Generated by Django 2.1.11 on 2019-08-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerconfig',
            name='height',
            field=models.IntegerField(default=200, max_length=6, verbose_name='Height in Pixels'),
        ),
    ]
