"""Signals for Drivers App."""

import os
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import Driver


@receiver(pre_save, sender=Driver)
def delete_sensitive_documents(sender, instance, **kwargs):
    """Delete sensitive documents associated with a driver if they are verified."""
    if instance.is_verified:
        try:
            if instance.driver_license:
                os.remove(
                    os.path.join(settings.MEDIA_ROOT, instance.driver_license.name)
                )
            if instance.identification_document:
                os.remove(
                    os.path.join(
                        settings.MEDIA_ROOT, instance.identification_document.name
                    )
                )
            if instance.social_security_certificate:
                os.remove(
                    os.path.join(
                        settings.MEDIA_ROOT, instance.social_security_certificate.name
                    )
                )
        except FileNotFoundError:
            # logger.error(f"File not found error")
            # ! TODO: Add sentry for logs
            pass
