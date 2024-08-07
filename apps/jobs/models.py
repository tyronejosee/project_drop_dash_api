"""Models for Jobs App."""

from django.conf import settings
from django.db import models

from apps.utilities.models import BaseModel
from apps.locations.models import Country, State, City
from .managers import PositionManager, WorkerManager, ApplicantManager
from .choices import StatusChoices, ContractTypeChoices, WorkerStatusChoices

User = settings.AUTH_USER_MODEL


class Position(BaseModel):
    """Model definition for Position."""

    position = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    objects = PositionManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "position"
        verbose_name_plural = "positions"

    def __str__(self):
        return str(self.position)


class Worker(BaseModel):
    """Model definition for Worker."""

    user_id = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city_id = models.ForeignKey(City, on_delete=models.PROTECT)
    state_id = models.ForeignKey(State, on_delete=models.PROTECT)
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT)
    position_id = models.ForeignKey(Position, on_delete=models.PROTECT)
    hired_date = models.DateField()
    termination_date = models.DateField(null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    contract_type = models.CharField(
        max_length=25,
        choices=ContractTypeChoices.choices,
        default=ContractTypeChoices.FIXED_TERM,
    )
    status = models.CharField(
        max_length=10,
        choices=WorkerStatusChoices.choices,
        default=WorkerStatusChoices.ACTIVE,
    )
    contract_file = models.FileField(
        upload_to="jobs/contracts/",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Indicates if the worker is currently active.",
    )
    is_full_time = models.BooleanField(
        default=False,
        help_text="Indicates if the worker is employed full-time.",
    )

    objects = WorkerManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "worker"
        verbose_name_plural = "workers"
        indexes = [
            models.Index(fields=["is_active"]),
            models.Index(fields=["is_full_time"]),
        ]

    def __str__(self):
        return str(self.user_id)


class Applicant(BaseModel):
    """Model definition for Applicant."""

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    position_id = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        help_text="Applied for position...",
    )
    cv = models.FileField(upload_to="jobs/applicants/cv/")
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )

    objects = ApplicantManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "applicant"
        verbose_name_plural = "applicants"

    def __str__(self):
        return str(self.user_id)
