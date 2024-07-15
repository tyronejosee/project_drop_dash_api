"""Choices for Jobs App."""

from django.db.models import TextChoices


class StatusChoices(TextChoices):

    PENDING = "pending", "Pending"
    REVIEWED = "reviewed", "Reviewed"
    ACCEPTED = "accepted", "Accepted"
    REJECTED = "rejected", "Rejected"


class ContractTypeChoices(TextChoices):

    FIXED_TERM = "fixed_term", "Fixed-term Contract"
    PROJECT_BASED = "project_based", "Project-based Contract"
    PART_TIME = "part_time", "Part-time Contract"
    INTERN = "intern", "Internship Contract"
    FOREIGN = "foreign", "Foreign Worker Contract"
    ART_AND_ENTERTAINMENT = "art_and_entertainment", "Art and Entertainment Contract"
    FEE_BASED = "fee_based", "Fee-based Contract"
    INDEFINITE = "indefinite", "Indefinite Contract"
