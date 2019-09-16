from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cms_plugins.models import BannerConfig, LightSliderConfig


class BannerPlugin(CMSPluginBase):
    model = BannerConfig
    render_template = 'banner.html'
    name = "Banner Plugin"
    allow_children = True
    child_classes = [
        'Bootstrap4CardPlugin',
        'Bootstrap4CardInnerPlugin',
        'Bootstrap4LinkPlugin',
        'Bootstrap4SpacingPlugin',
        'TextPlugin',
    ]

    def render(self, context, instance, placeholder):
        context = super(BannerPlugin, self).render(context, instance, placeholder)
        context.update({'instance': instance})

        return context


plugin_pool.register_plugin(BannerPlugin)


class LightSliderGallery(CMSPluginBase):
    model = LightSliderConfig
    name = "Light Slider Gallery"
    render_template = "light_slider_gallery.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'images': instance.get_folder_images(),
        })
        return context


plugin_pool.register_plugin(LightSliderGallery)
