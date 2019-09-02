from cms.models import CMSPlugin, models, PlaceholderField
from django.db.models import IntegerField, FloatField
from filer.fields.image import FilerImageField

from cms_plugins.constants import TEXT_COLOR_CHOICES, WIDTH_CHOICES, TEXT_ALIGNMENT_CHOICES


class BannerConfig(CMSPlugin):
    background_image = FilerImageField(
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    width = models.CharField(
        verbose_name="Width",
        choices=WIDTH_CHOICES,
        default="full-width",
        max_length=255,
    )
    height = models.IntegerField(
        verbose_name="Height in Pixels",
        default=200
    )

    class Meta:
        db_table = 'banner_plugin'
        verbose_name_plural = 'Banner Plugins'

    def __str__(self):

        return self.background_image.url
