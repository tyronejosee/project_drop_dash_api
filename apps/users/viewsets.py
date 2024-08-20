"""ViewSets for Users App."""

from djoser.views import UserViewSet
from drf_spectacular.utils import extend_schema_view

from .schemas import user_schemas


@extend_schema_view(**user_schemas)
class UserExtensionViewSet(UserViewSet):
    """Pending."""

    pass
