from django.urls import path

from custom_admin.views import PingGoogleView

urlpatterns = [
    path("ping-google/", PingGoogleView.as_view(), name="pinggoogle"),
]
