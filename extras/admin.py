from django.contrib import admin

# Register your models here.
from extras.models import Extra


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ('motive',)
