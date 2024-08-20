"""ViewSets for Users App."""

from djoser.views import UserViewSet
from drf_spectacular.utils import extend_schema_view

from .schemas import user_schemas


@extend_schema_view(**user_schemas)
class UserExtensionViewSet(UserViewSet):
    """
    Extended viewset for user-related operations.

    This viewset extends the standard UserViewSet from djoser (`djoser.views`),
    to include custom schema documentation using drf-spectacular.

    It inherits all functionalities of the original UserViewSet
    and applies additional schema customizations defined in `user_schemas`.
    """

    pass
