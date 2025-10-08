from django.db import migrations


def migrate_ai_contexts(apps, schema_editor):
    Team = apps.get_model("teams", "Team")
    AIContext = apps.get_model("ai", "AIContext")

    # Get the old context models
    WolfAIContext = apps.get_model("ai", "WolfAIContext")
    DragonAIContext = apps.get_model("ai", "DragonAIContext")
    HedgehogAIContext = apps.get_model("ai", "HedgehogAIContext")
    ChickenAIContext = apps.get_model("ai", "ChickenAIContext")
    EggAIContext = apps.get_model("ai", "EggAIContext")

    # Migrate contexts
    context_mappings = [
        (WolfAIContext, "wolf"),
        (DragonAIContext, "dragon"),
        (HedgehogAIContext, "hedgehog"),
        (ChickenAIContext, "chicken"),
        (EggAIContext, "egg"),
    ]

    for old_model, team_slug in context_mappings:
        try:
            old_context = old_model.objects.first()
            if old_context:
                team = Team.objects.get(slug=team_slug)
                AIContext.objects.create(team=team, context=old_context.context)
        except Exception as e:
            print(f"Error migrating {team_slug}: {e}")


def reverse_migration(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        (
            "ai",
            "0003_create_aicontext",
        ),
        ("teams", "0002_migrate_existing_teams"),
    ]

    operations = [
        migrations.RunPython(migrate_ai_contexts, reverse_migration),
    ]
