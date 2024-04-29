"""URLs for Foods App."""

from django.urls import path

from .views import FoodListView, FoodDetailView, FoodDeletedListView


urlpatterns = [
    path("api/v1/foods/", FoodListView.as_view()),
    path("api/v1/foods/<uuid:food_id>/", FoodDetailView.as_view()),
    path("api/v1/foods/deleted/", FoodDeletedListView.as_view()),
]
