"""URLs for config project."""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    # Temp urls
    path("", RedirectView.as_view(url="/admin/")),
    # Admin urls
    path("admin/", admin.site.urls),
    # Schemas urls
    path(
        "api/schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Apps routers
    path("", include("apps.restaurants.routers")),
    path("", include("apps.promotions.routers")),
    path("", include("apps.locations.routers")),
    path("", include("apps.blogs.routers")),
    path("", include("apps.home.routers")),
    path("", include("apps.jobs.routers")),
    path("", include("apps.orders.routers")),
    path("", include("apps.drivers.routers")),
    # Apps urls
    path("", include("apps.users.urls")),
    # ! TODO: Remove urls
    # path("", include("apps.orders.urls")),
    # path("", include("apps.restaurants.urls")),
    # path("", include("apps.promotions.urls")),
]


# Debug config
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]


# AdminSite props.
admin.site.site_header = "Drop Dash"
admin.site.site_title = "Drop Dash"
admin.site.index_title = "Admin"
