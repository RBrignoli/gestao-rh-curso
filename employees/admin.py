from django.contrib import admin

# Register your models here.
from employees.models import Employees


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name',)
