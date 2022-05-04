from django.db import models

# Create your models here.
from helpers.models import TimestampModel


class Documents(TimestampModel):
    description = models.CharField(
        max_length=200
    )
    title = models.CharField(
        max_length=12
    )

    def __str__(self):
        return self.title
