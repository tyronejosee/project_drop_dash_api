"""URLs for Categories App."""

from django.urls import path

from .views import CategoryList, CategoryDetail


urlpatterns = [
    path(
        "api/v1/categories/",
        CategoryList.as_view()
    ),
    path(
        "api/v1/categories/<uuid:category_id>/",
        CategoryDetail.as_view()
    )
]
