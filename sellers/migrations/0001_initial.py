# Generated by Django 2.1.11 on 2019-09-03 02:00

import django.core.validators
from django.db import migrations, models
import re
import sellers.utilities


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$"), 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')], verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$"), 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')], verbose_name='Last name')),
                ('email', models.EmailField(max_length=255, verbose_name='Email address')),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, validators=[sellers.utilities.validate_phone_number])),
                ('is_phone_mobile', models.BooleanField(default=False)),
                ('permission_to_text', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$"), 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')], verbose_name='Street address')),
                ('city', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(re.compile("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$"), 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')], verbose_name='City')),
                ('zip_code', models.CharField(max_length=10, validators=[sellers.utilities.validate_zip], verbose_name='Zip code')),
                ('property_type', models.CharField(choices=[('', 'Select property type...'), ('single_family', 'Single family home'), ('multi_family', 'Multi-family home'), ('manufactured', 'Manufactured home'), ('condo', 'Condo / co-op'), ('apartment', 'Apartment'), ('town_home', 'Town home'), ('lots_land', 'Lots / land')], default='single_family', max_length=25)),
            ],
        ),
    ]
