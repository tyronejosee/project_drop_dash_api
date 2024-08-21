"""Managers for Jobs App."""

from apps.utilities.managers import BaseManager


class PositionManager(BaseManager):
    """Manager for Position Model."""

    def get_list(self):
        return self.get_available().defer("description")


class WorkerManager(BaseManager):
    """Manager for Worker Model."""

    def get_list(self):
        return (
            self.get_available()
            .select_related(
                "user_id",
                "position_id",
            )
            .only(
                "id",
                "user_id",
                "position_id",
                "status",
                "contract_type",
                "is_active",
            )
        )

    def get_detail(self):
        return self.get_available().select_related(
            "user_id",
            "city_id",
            "state_id",
            "country_id",
            "position_id",
        )


class ApplicantManager(BaseManager):
    """Manager for Applicant Model."""

    def get_list(self):
        return (
            self.get_available()
            .select_related(
                "user_id",
                "position_id",
            )
            .only(
                "id",
                "user_id",
                "position_id",
                "status",
            )
        )

    def get_detail(self):
        return self.get_available().select_related(
            "user_id",
            "position_id",
        )
