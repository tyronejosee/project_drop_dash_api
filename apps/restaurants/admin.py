"""Admin for Restaurants App."""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from apps.utilities.admin import BaseAdmin
from apps.reviews.models import Review
from .models import Restaurant, Category, Food


class ReviewInline(GenericTabularInline):
    model = Review


@admin.register(Restaurant)
class RestaurantAdmin(BaseAdmin):
    """Admin for Restaurant model."""

    search_fields = ["name", "user"]
    list_display = ["name", "is_verified", "is_available"]
    list_editable = ["is_available"]
    list_filter = ["specialty", "is_open"]
    readonly_fields = ["pk", "slug", "is_open", "created_at", "updated_at"]
    ordering = ["name"]
    inlines = [ReviewInline]


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    """Admin for Category model."""

    list_per_page = 25
    search_fields = ["name", "restaurant"]
    list_display = ["name", "restaurant", "is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["name"]


@admin.register(Food)
class FoodAdmin(BaseAdmin):
    """Admin for Food model."""

    search_fields = ["name", "restaurant"]
    list_display = ["name", "restaurant", "is_available", "created_at", "updated_at"]
    list_editable = ["is_available"]
    list_filter = ["restaurant", "category"]
    readonly_fields = ["pk", "sale_price", "created_at", "updated_at"]
    autocomplete_fields = ["restaurant", "category"]
    ordering = ["pk"]
