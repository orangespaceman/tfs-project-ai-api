from django.db import migrations
from django.contrib.auth.models import User


def create_teams_and_users(apps, schema_editor):
    Team = apps.get_model("teams", "Team")
    TeamMember = apps.get_model("teams", "TeamMember")
    User = apps.get_model("auth", "User")

    teams_data = [
        {"name": "Wolf", "slug": "wolf"},
        {"name": "Dragon", "slug": "dragon"},
        {"name": "Hedgehog", "slug": "hedgehog"},
        {"name": "Chicken", "slug": "chicken"},
        {"name": "Egg", "slug": "egg"},
    ]

    for team_data in teams_data:
        team = Team.objects.create(**team_data)

        # Create a user for this team
        username = f"{team_data['slug']}"
        user = User.objects.create_user(
            username=username,
            email=f"{username}@example.com",
            password="...",
        )

        # Create team member relationship
        TeamMember.objects.create(user=user, team=team)


def reverse_migration(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_teams_and_users, reverse_migration),
    ]
