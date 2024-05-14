from django.db import models


class AbstractAIContext(models.Model):
    context = models.CharField(
        max_length=255,
        help_text="Text to be passed to ChatGPT as extra context prior to processing user input",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.context


class WolfAIContext(AbstractAIContext):
    class Meta:
        verbose_name = "Wolf AI Context"
        verbose_name_plural = "Wolf AI Context"


class DragonAIContext(AbstractAIContext):
    class Meta:
        verbose_name = "Dragon AI Context"
        verbose_name_plural = "Dragon AI Context"


class HedgehogAIContext(AbstractAIContext):
    class Meta:
        verbose_name = "Hedgehog AI Context"
        verbose_name_plural = "Hedgehog AI Context"
