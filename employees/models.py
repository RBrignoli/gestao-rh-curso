from django.db import models

# Create your models here.
from helpers.models import TimestampModel


class Employees(TimestampModel):
    name = models.CharField(
        max_length=36
    )
    document_number = models.CharField(
        max_length=12
    )

    def __str__(self):
        return self.name
