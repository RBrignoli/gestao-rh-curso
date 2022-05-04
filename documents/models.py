from django.db import models

# Create your models here.
from employees.models import Employees
from helpers.models import TimestampModel


class Documents(TimestampModel):
    description = models.CharField(
        max_length=200
    )
    title = models.CharField(
        max_length=12
    )
    owner = models.ForeignKey(
        Employees,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
)

    def __str__(self):
        return self.title
