from django.urls import path

from .views import MenuAPIView

urlpatterns = [
    path("api/v1/menus/", MenuAPIView.as_view()),
    # path("api/v1/menus/<uuid:menu_id>"),
]
