"""URLs for Promotions App."""

from django.urls import path

from .views import PromotionListView, PromotionDetailView, PromotionSearchView


urlpatterns = [
    path(
        "api/v1/promotions/",
        PromotionListView.as_view()
    ),
    path(
        "api/v1/promotions/<uuid:promotion_id>/",
        PromotionDetailView.as_view()
    ),
    path(
        "api/v1/promotions/search/",
        PromotionSearchView.as_view()
    )
]
