from django.core.validators import RegexValidator
from django.db import models

from sellers.utilities import alphanum_pattern, validate_phone_number, validate_zip

alphanumeric = RegexValidator(
    alphanum_pattern,
    'Only letters, numbers, spaces and '
    '&#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;'
    '&#58;&#44;&#46;&#33;&#63; are allowed here.'
)


class SellerProfile(models.Model):
    """Contact information about a potential seller"""
    SINGLE_FAMILY_HOME = "single_family"
    MULTI_FAMILY_HOME = "multi_family"
    CONDO = "condo"
    MANUFACTURED = "manufactured"
    APARTMENT = "apartment"
    TOWN_HOME = "town_home"
    LOTS_LAND = "lots_land"
    PROPERTY_TYPE_CHOICES = (
        ('', 'Select property type...'),
        (SINGLE_FAMILY_HOME, 'Single family home'),
        (MULTI_FAMILY_HOME, 'Multi-family home'),
        (MANUFACTURED, 'Manufactured home'),
        (CONDO, 'Condo / co-op'),
        (APARTMENT, 'Apartment'),
        (TOWN_HOME, 'Town home'),
        (LOTS_LAND, 'Lots / land'),
    )
    first_name = models.CharField(max_length=30,
                                  verbose_name="First name",
                                  validators=[alphanumeric])
    last_name = models.CharField(max_length=30,
                                 verbose_name="Last name",
                                 validators=[alphanumeric])
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255
    )
    phone_number = models.CharField(max_length=10,
                                    blank=True,
                                    null=True,
                                    validators=[validate_phone_number])
    is_phone_mobile = models.BooleanField(default=False)
    permission_to_text = models.BooleanField(default=False)
    address = models.CharField(max_length=100,
                               verbose_name="Street address",
                               validators=[alphanumeric])
    city = models.CharField(max_length=50,
                            verbose_name="City",
                            validators=[alphanumeric])
    zip_code = models.CharField(max_length=10,
                                verbose_name="Zip code",
                                validators=[validate_zip])
    property_type = models.CharField(max_length=25,
                                     choices=PROPERTY_TYPE_CHOICES,
                                     default=SINGLE_FAMILY_HOME)
