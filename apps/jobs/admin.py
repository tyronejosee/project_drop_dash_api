"""Admin for Jobs App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Position, Worker, Applicant


@admin.register(Position)
class PositionAdmin(BaseAdmin):
    """Admin for Position model."""

    search_fields = ["position"]
    list_display = ["position", "is_available"]
    list_editable = ["is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(Worker)
class WorkerAdmin(BaseAdmin):
    """Admin for Worker model."""

    search_fields = ["user_id", "position_id"]
    list_display = ["user_id", "is_available"]
    list_editable = ["is_available"]
    list_filter = ["contract_type"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(Applicant)
class ApplicantAdmin(BaseAdmin):
    """Admin for Applicant model."""

    search_fields = ["user_id", "position_id"]
    list_display = ["user_id", "position_id", "status", "is_available"]
    list_editable = ["is_available"]
    list_filter = ["status"]
    readonly_fields = ["pk", "created_at", "updated_at"]
