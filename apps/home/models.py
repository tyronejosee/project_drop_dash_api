"""Models for Home App."""

from django.db import models

from apps.utilities.models import BaseModel
from apps.utilities.mixins import SlugMixin
from .managers import CompanyManager, PageManager, KeywordManager


class Company(BaseModel):
    """Model definition for Company."""

    name = models.CharField(
        max_length=50,
        help_text="Name of the company",
    )
    logo = models.FileField(
        upload_to="company/",
        help_text="Logo of the company",
    )
    description = models.TextField(
        help_text="Description of the company",
    )
    rights = models.CharField(
        max_length=50,
        help_text="Copyrights of the company",
    )
    email = models.EmailField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    github = models.URLField(blank=True)

    objects = CompanyManager()

    class Meta:
        ordering = ["name"]
        verbose_name = "company"
        verbose_name_plural = "company"

    def __str__(self):
        return str(self.name)


class Page(BaseModel, SlugMixin):
    """Model definition for Page."""

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique key for the page, ex: About Us, Legal, etc",
    )
    content = models.TextField(help_text="Content of the page")

    objects = PageManager()

    class Meta:
        ordering = ["name"]
        verbose_name = "page"
        verbose_name_plural = "pages"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)


class Keyword(BaseModel, SlugMixin):
    """Model definition for Keyword."""

    word = models.CharField(max_length=20, unique=True)

    objects = KeywordManager()

    class Meta:
        ordering = ["word"]
        verbose_name = "keyword"
        verbose_name_plural = "keywords"

    def __str__(self):
        return str(self.word)

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)
