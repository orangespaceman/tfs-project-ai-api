from django.db import migrations


def migrate_products(apps, schema_editor):
    Team = apps.get_model("teams", "Team")
    Product = apps.get_model("products", "Product")

    # Get the old product models
    WolfProduct = apps.get_model("products", "WolfProduct")
    DragonProduct = apps.get_model("products", "DragonProduct")
    HedgehogProduct = apps.get_model("products", "HedgehogProduct")
    ChickenProduct = apps.get_model("products", "ChickenProduct")
    EggProduct = apps.get_model("products", "EggProduct")

    # Migrate products
    product_mappings = [
        (WolfProduct, "wolf"),
        (DragonProduct, "dragon"),
        (HedgehogProduct, "hedgehog"),
        (ChickenProduct, "chicken"),
        (EggProduct, "egg"),
    ]

    for old_model, team_slug in product_mappings:
        try:
            team = Team.objects.get(slug=team_slug)
            for old_product in old_model.objects.all():
                Product.objects.create(
                    team=team,
                    title=old_product.title,
                    description=old_product.description,
                    price=old_product.price,
                    stars=old_product.stars,
                    image=old_product.image,
                    created_date=old_product.created_date,
                    modified_date=old_product.modified_date,
                    uuid=old_product.uuid,
                )
        except Exception as e:
            print(f"Error migrating {team_slug} products: {e}")


def reverse_migration(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        (
            "products",
            "0003_product_delete_chickenproduct_delete_dragonproduct_and_more",
        ),
        ("teams", "0002_migrate_existing_teams"),
    ]

    operations = [
        migrations.RunPython(migrate_products, reverse_migration),
    ]
