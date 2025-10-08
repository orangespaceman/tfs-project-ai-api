from django.urls import path
from . import views

urlpatterns = [
    path("<str:team_slug>/", views.team_ai_query, name="team_ai_query"),
]
