"""Models for Jobs App."""

from django.conf import settings
from django.db import models

from apps.utilities.models import BaseModel
from apps.locations.models import Country, State, City
from .choices import StatusChoices, ContractTypeChoices

User = settings.AUTH_USER_MODEL


class Position(BaseModel):
    """Model definition for JobPosition (Catalog)."""

    position = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["pk"]
        verbose_name = "position"
        verbose_name_plural = "positions"

    def __str__(self):
        return str(self.position)


class Worker(BaseModel):
    """Model definition for Worker (Entity)."""

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    hired_date = models.DateField()
    termination_date = models.DateField(null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    contract_type = models.CharField(
        max_length=25,
        choices=ContractTypeChoices.choices,
        default=ContractTypeChoices.FIXED_TERM,
    )
    contract_file = models.FileField(
        upload_to="jobs/contracts/",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return str(self.user)


class Applicant(BaseModel):
    """Model definition for Applicant (Entity)."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    applied_for = models.ForeignKey(Position, on_delete=models.CASCADE)
    cv = models.FileField(upload_to="jobs/applicants/cv/")
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = "applicant"
        verbose_name_plural = "applicants"

    def __str__(self):
        return str(self.user)
