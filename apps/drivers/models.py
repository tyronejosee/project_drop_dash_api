"""Models for Contents App."""

from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator

from apps.utilities.models import BaseModel
from apps.utilities.paths import docs_path
from apps.locations.models import Country, State, City
from .managers import DriverManager, ResourceManager
from .choices import Status, ResourceType, RequestStatus

User = settings.AUTH_USER_MODEL


class Driver(BaseModel):
    """Model definition for Driver."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=100)
    driver_license = models.FileField(
        upload_to=docs_path,
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
    address = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    is_verified = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.BRONCE
    )

    # TODO: Add crontab or signals for logic, Add more validators

    objects = DriverManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return str(self.user.username)


class Resource(BaseModel):
    """Model definition for Resource."""

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    resource_type = models.CharField(
        max_length=15, choices=ResourceType.choices, default=ResourceType.BACKPACKS
    )
    note = models.TextField(blank=True)
    status = models.CharField(
        max_length=15, choices=RequestStatus.choices, default=RequestStatus.PENDING
    )
    # request_date = created_at (BaseModel)

    objects = ResourceManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "resource"
        verbose_name_plural = "resources"

    def __str__(self):
        return f"Resources for {self.driver}"
