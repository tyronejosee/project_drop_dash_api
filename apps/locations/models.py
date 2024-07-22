"""Models for Locations App."""

from django.db import models

from apps.utilities.models import BaseModel
from .managers import CountryManager, StateManager, CityManager


class Country(BaseModel):
    """Model definition for Country."""

    name = models.CharField(max_length=100, unique=True)

    objects = CountryManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "country"
        verbose_name_plural = "countries"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return str(self.name)


class State(BaseModel):
    """Model definition for State."""

    name = models.CharField(max_length=100, unique=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    objects = StateManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "state"
        verbose_name_plural = "states"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return str(self.name)


class City(BaseModel):
    """Model definition for City."""

    name = models.CharField(max_length=100, unique=True)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)

    objects = CityManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "city"
        verbose_name_plural = "cities"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return str(self.name)
