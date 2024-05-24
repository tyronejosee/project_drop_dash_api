"""Models for Locations App."""

from django.db import models

from apps.utilities.models import BaseModel


class Country(BaseModel):
    """Model definition for Country."""

    name = models.CharField(max_length=100, unique=True)

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
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

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
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        ordering = ["pk"]
        verbose_name = "city"
        verbose_name_plural = "cities"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return str(self.name)


# class Address(models.Model):
#     """Model definition for Address."""

#     street = models.CharField(max_length=100)
#     city = models.ForeignKey(City, on_delete=models.PROTECT)
#     state = models.ForeignKey(State, on_delete=models.PROTECT)
#     country = models.ForeignKey(Country, on_delete=models.PROTECT)
