"""Managers for Jobs App."""

from apps.utilities.managers import BaseManager


class PositionManager(BaseManager):
    """Manager for Position Model."""


class WorkerManager(BaseManager):
    """Manager for Worker Model."""


class ApplicantManager(BaseManager):
    """Manager for Applicant Model."""
