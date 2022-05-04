from django.db import models

# Create your models here.
from helpers.models import TimestampModel


class Extra(TimestampModel):
    motive = models.CharField(
        max_length=36
    )
    quantity = models.PositiveIntegerField(
    )

    def __str__(self):
        return self.motive
