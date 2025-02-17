from django.urls import path

from . import views

urlpatterns = [
    path("wolf", views.wolf, name="wolf"),
    path("dragon", views.dragon, name="dragon"),
    path("hedgehog", views.hedgehog, name="hedgehog"),
    path("chicken", views.chicken, name="chicken"),
    path("egg", views.egg, name="egg"),
]
