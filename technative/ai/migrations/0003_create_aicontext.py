import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ai", "0002_chickenaicontext_eggaicontext_and_more"),
        ("teams", "0002_migrate_existing_teams"),
    ]

    operations = [
        migrations.CreateModel(
            name="AIContext",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "context",
                    models.CharField(
                        help_text="Text to be passed to ChatGPT as extra context prior to processing user input",
                        max_length=255,
                    ),
                ),
                (
                    "team",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="teams.team"
                    ),
                ),
            ],
            options={
                "verbose_name": "AI Context",
                "verbose_name_plural": "AI Contexts",
            },
        ),
    ]
