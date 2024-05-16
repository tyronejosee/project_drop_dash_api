"""Models for Contents App."""

from django.conf import settings
from django.db import models

from apps.utilities.validators import validate_phone, validate_birth_date
from apps.utilities.models import BaseModel
from apps.locations.models import Country, State, City
from .managers import DriverManager
from .choices import Status

User = settings.AUTH_USER_MODEL


class Driver(BaseModel):
    """Model definition for Driver (Entity)."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12, unique=True, validators=[validate_phone])
    email = models.EmailField(blank=True)
    birth_date = models.DateField(validators=[validate_birth_date])
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.BRONCE
    )  # TODO: Add crontab or signals for logic

    objects = DriverManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return str(self.user.username)
