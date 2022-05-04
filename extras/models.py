from django.db import models

# Create your models here.
from employees.models import Employees
from helpers.models import TimestampModel


class Extra(TimestampModel):
    motive = models.CharField(
        max_length=36
    )
    quantity = models.PositiveIntegerField(
    )
    Employee = models.ForeignKey(
        Employees,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.motive
