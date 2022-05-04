from django.db import models

# Create your models here.
from helpers.models import TimestampModel


class Department(TimestampModel):
    name = models.CharField(
        max_length=70
    )


    def __str__(self):
        return self.name