from aldryn_newsblog.sitemaps import NewsBlogSitemap
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.sites.models import Site
from django.urls import path, include


class SiteMapDomainMixin(Sitemap):
    around_domain = "aroundsyracuserealty.com"

    def get_urls(self, page=1, site=None, protocol=None):
        fake_site = Site(domain=self.around_domain, name=self.around_domain)

        return super(SiteMapDomainMixin, self).get_urls(page, fake_site, protocol=None)


class AroundCMSSitemap(SiteMapDomainMixin, CMSSitemap):
    changefreq = "weekly"
    priority = 0.5


sitemaps = {
    "cmspages": AroundCMSSitemap,
    "blog": NewsBlogSitemap
}


urlpatterns = [
    path('around-admin/', admin.site.urls),
    path("custom-admin/", include("custom_admin.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    url(r'^sharing/', include('filer.urls')),
    path("sellers/", include("sellers.urls")),
    url(r'^', include('cms.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
