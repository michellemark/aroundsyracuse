# Generated by Django 2.1.11 on 2019-09-01 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0004_bannerconfig_banner_content_placement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerconfig',
            name='banner_content',
        ),
    ]
