from django.db import models
from teams.models import Team


class AIContext(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    context = models.CharField(
        max_length=255,
        help_text="Text to be passed to ChatGPT as extra context prior to processing user input",
    )

    class Meta:
        verbose_name = "AI Context"
        verbose_name_plural = "AI Contexts"

    def __str__(self):
        return f"{self.team.name} AI Context"
