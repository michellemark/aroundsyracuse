from cms.models import CMSPlugin, models
from filer.fields.folder import FilerFolderField
from filer.fields.image import FilerImageField
from filer.models import Image

from cms_plugins.constants import WIDTH_CHOICES


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


class LightSliderConfig(CMSPlugin):
    gallery_folder = FilerFolderField(
        verbose_name='Folder',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'light_slider_plugin'
        verbose_name_plural = 'Light Slider Plugins'

    def __str__(self):

        return self.gallery_folder.name

    def get_folder_images(self):
        images = self.gallery_folder.files.instance_of(Image)

        return images.filter(is_public=True)
