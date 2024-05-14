import uuid
from django.db import models


class AbstractProduct(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(
        blank=True,
        null=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stars = models.IntegerField(
        default=0,
        choices=[
            (1, "1 star"),
            (2, "2 stars"),
            (3, "3 stars"),
            (4, "4 stars"),
            (5, "5 stars"),
        ],
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class WolfProduct(AbstractProduct):
    image = models.ImageField(upload_to="images/products/wolf/")


class DragonProduct(AbstractProduct):
    image = models.ImageField(upload_to="images/products/dragon/")


class HedgehogProduct(AbstractProduct):
    image = models.ImageField(upload_to="images/products/hedgehog/")
