"""Choices for Utilities App."""

from django.db.models import TextChoices


class SortChoices(TextChoices):

    ASC = "asc", "Ascending"
    DESC = "desc", "Descending"
