"""Admin for Home App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Company, Page, Keyword


@admin.register(Company)
class CompanyAdmin(BaseAdmin):
    """Admin for Company model."""

    list_display = ["name", "created_at"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(Page)
class PageAdmin(BaseAdmin):
    """Admin for Page model."""

    search_fields = ["name"]
    list_display = ["name", "is_available", "created_at"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(Keyword)
class KeywordAdmin(BaseAdmin):
    """Admin for Keyword model."""

    search_fields = ["word"]
    list_display = ["word", "is_available", "created_at"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]
