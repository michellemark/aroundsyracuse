# Generated by Django 2.1.11 on 2019-09-03 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0006_remove_bannerconfig_banner_content_placement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerconfig',
            name='height',
            field=models.IntegerField(default=200, verbose_name='Height in Pixels'),
        ),
    ]
