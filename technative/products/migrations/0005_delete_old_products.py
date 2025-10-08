from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_migrate_products"),
    ]

    operations = [
        migrations.DeleteModel(name="ChickenProduct"),
        migrations.DeleteModel(name="DragonProduct"),
        migrations.DeleteModel(name="EggProduct"),
        migrations.DeleteModel(name="HedgehogProduct"),
        migrations.DeleteModel(name="WolfProduct"),
    ]
