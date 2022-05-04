from django.db import models

# Create your models here.
from companies.models import Company
from departments.models import Department
from helpers.models import TimestampModel

from django.contrib.auth.models import User


class Employees(TimestampModel):
    name = models.CharField(
        max_length=36
    )
    document_number = models.CharField(
        max_length=12
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    departments = models.ManyToManyField(
        Department
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )



    def __str__(self):
        return self.name
