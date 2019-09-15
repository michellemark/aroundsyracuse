from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

sitemaps = {
    "cmspages": CMSSitemap
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
