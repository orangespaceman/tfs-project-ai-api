import uuid
from django.db import models
from teams.models import Team


class Product(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
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
    image = models.ImageField(upload_to="images/products/")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
