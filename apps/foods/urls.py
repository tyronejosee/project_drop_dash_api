"""URLs for Foods App."""

from django.urls import path

from .views import FoodList, FoodDetail


urlpatterns = [
    path("api/v1/foods/", FoodList.as_view()),
    path("api/v1/foods/<uuid:food_id>/", FoodDetail.as_view())
]
