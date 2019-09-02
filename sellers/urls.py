from django.urls import path

from sellers.views import SellerProfileView

urlpatterns = [
    path("free-evaluation-step1/", SellerProfileView.as_view(), name="sellerstep1"),
]
