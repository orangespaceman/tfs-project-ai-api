from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ai", "0004_migrate_ai_contexts"),
    ]

    operations = [
        migrations.DeleteModel(name="ChickenAIContext"),
        migrations.DeleteModel(name="DragonAIContext"),
        migrations.DeleteModel(name="EggAIContext"),
        migrations.DeleteModel(name="HedgehogAIContext"),
        migrations.DeleteModel(name="WolfAIContext"),
    ]
