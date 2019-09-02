from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('around-admin/', admin.site.urls),
    url(r'^sharing/', include('filer.urls')),
    path("sellers/", include("sellers.urls")),
    url(r'^', include('cms.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
