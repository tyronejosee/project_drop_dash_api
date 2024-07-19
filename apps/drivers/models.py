"""Models for Contents App."""

from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator

from apps.utilities.models import BaseModel
from apps.utilities.paths import docs_path
from apps.locations.models import Country, State, City
from .managers import DriverManager, ResourceManager
from .choices import (
    VehicleChoices,
    StatusChoices,
    ResourceTypeChoices,
    RequestStatusChoices,
)

User = settings.AUTH_USER_MODEL


class Driver(BaseModel):
    """Model definition for Driver."""

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=100)
    driver_license = models.FileField(
        upload_to=docs_path,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["pdf", "jpg"])],
    )
    identification_document = models.FileField(
        upload_to=docs_path,
        validators=[FileExtensionValidator(["pdf", "jpg"])],
    )
    social_security_certificate = models.FileField(
        upload_to=docs_path,
        validators=[FileExtensionValidator(["pdf", "jpg"])],
    )
    criminal_record_certificate = models.FileField(
        upload_to=docs_path,
        validators=[FileExtensionValidator(["pdf", "jpg"])],
    )
    address = models.CharField(max_length=100)
    city_id = models.ForeignKey(City, on_delete=models.PROTECT)
    state_id = models.ForeignKey(State, on_delete=models.PROTECT)
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT)
    vehicle_type = models.CharField(max_length=15, choices=VehicleChoices.choices)
    is_verified = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.BRONCE,
    )

    objects = DriverManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return str(self.user_id.username)


class Resource(BaseModel):
    """Model definition for Resource."""

    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    resource_type = models.CharField(
        max_length=15,
        choices=ResourceTypeChoices.choices,
    )
    note = models.TextField(blank=True)
    status = models.CharField(
        max_length=15,
        choices=RequestStatusChoices.choices,
        default=RequestStatusChoices.PENDING,
    )

    objects = ResourceManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "resource"
        verbose_name_plural = "resources"

    def __str__(self):
        return f"Resources for {self.driver_id}"
