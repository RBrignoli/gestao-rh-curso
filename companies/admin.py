from django.contrib import admin

# Register your models here.
from companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
