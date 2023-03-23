from django.db import models


class Information(models.Model):

    title = models.CharField(max_length=200)

    text = models.TextField(blank=True)

    order = models.IntegerField()

    class Meta:
        ordering = ("title", "order")
        verbose_name = "information"
        verbose_name_plural = "informations"

    def __str__(self) -> str:
        return self.title
