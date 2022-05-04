from django.contrib import admin

# Register your models here.
from documents.models import Documents


@admin.register(Documents)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',)
