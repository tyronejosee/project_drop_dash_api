"""Managers for Orders App."""

from apps.utilities.managers import BaseManager


class OrderManager(BaseManager):
    """Manager for Order Model."""

    def get_list_by_user(self, user):
        return (
            self.get_available()
            .filter(user_id=user)
            .select_related(
                "restaurant_id",
            )
            .only(
                "id",
                "shipping_name",
                "transaction",
                "restaurant_id",
                "amount",
                "status",
                "updated_at",
                "created_at",
            )
        )

    def get_detail_by_user(self, user):
        return (
            self.get_available()
            .filter(user_id=user)
            .select_related(
                "user_id",
                "city_id",
                "state_id",
                "country_id",
                "restaurant_id",
            )
        )

    def get_by_status(self, status):
        return self.get_available().filter(status=status)


class OrderItemManager(BaseManager):
    """Manager for OrderItem Model."""
