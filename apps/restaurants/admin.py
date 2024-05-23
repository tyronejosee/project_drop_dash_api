"""Admin for Restaurants App."""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from apps.reviews.models import Review
from .models import Restaurant, Category, Food


class ReviewInline(GenericTabularInline):
    model = Review


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Admin for Restaurant model."""

    list_per_page = 25
    search_fields = [
        "name",
        "user",
    ]
    list_display = [
        "name",
        "is_verified",
        "available",
    ]
    list_editable = [
        "available",
    ]
    list_filter = [
        "specialty",
        "is_open",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "is_open",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "name",
    ]
    inlines = [
        ReviewInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin for Category model."""

    list_per_page = 25
    search_fields = [
        "name",
        "restaurant",
    ]
    list_display = [
        "name",
        "restaurant",
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "name",
    ]


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    """Admin for Food model."""

    list_per_page = 25
    search_fields = [
        "name",
        "restaurant",
    ]
    list_display = [
        "name",
        "restaurant",
        "available",
        "created_at",
        "updated_at",
    ]
    list_editable = [
        "available",
    ]
    list_filter = [
        "restaurant",
        "category",
    ]
    readonly_fields = [
        "pk",
        "sale_price",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = [
        "restaurant",
        "category",
    ]
    ordering = [
        "pk",
    ]
