from django.db import models

# Create your models here.
from helpers.models import TimestampModel
from django.utils.translation import gettext_lazy as _


class Company(TimestampModel):
    name = models.CharField(
        max_length=256,
        verbose_name=_('Nome da MEI'),
    )

    cnpj = models.CharField(
        max_length=32,
        verbose_name=_('CNPJ da MEI'),
        unique=True,
        db_index=True
    )

    bank = models.CharField(
        max_length=256,
        verbose_name=_('Banco'),
    )

    agency = models.CharField(
        max_length=32,
        verbose_name=_('Agência'),
    )

    account_number = models.CharField(
        max_length=32,
        verbose_name=_('Conta'),
    )

    class Meta:
        verbose_name_plural = _('MEIs')
        verbose_name = _('MEI')
