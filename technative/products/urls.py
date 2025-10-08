from django.urls import path
from . import views

urlpatterns = [
    path("<str:team_slug>/", views.team_products, name="team_products"),
]
