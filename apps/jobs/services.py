"""Services for Jobs App."""

from .choices import WorkerStatusChoices


class PositionService:
    """
    Service for Position model.
    """

    pass


class WorkerService:
    """
    Service for Worker model.
    """

    @staticmethod
    def terminate_worker(worker):
        """Terminate a worker's contract."""
        worker.status = WorkerStatusChoices.TERMINATED
        worker.is_active = False
        worker.is_full_time = False
        worker.save()
        return worker


class ApplicantService:
    """
    Service for Applicant model.
    """

    pass
