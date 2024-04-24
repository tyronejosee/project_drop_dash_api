"""URLs for config project."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)


urlpatterns = [
    # Admin urls
    path("admin/", admin.site.urls),

    # Schemas urls
    path("api/schema/swagger/",
         SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/schema/redoc/",
         SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Apps urls
    path("", include("apps.categories.urls")),
    path("", include("apps.restaurants.urls")),
    path("", include("apps.drivers.urls")),
    path("", include("apps.foods.urls")),
    path("", include("apps.orders.urls")),
    path("", include("apps.coupons.urls")),
    path("", include("apps.users.urls")),
]


# Debug config
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# AdminSite props.
admin.site.site_header = "Drop Dash"
admin.site.site_title = "Drop Dash"
admin.site.index_title = "Admin"
