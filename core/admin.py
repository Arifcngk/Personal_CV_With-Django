from django.contrib import admin
from core.models import *


# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameters', 'updated_data', 'created_data']
    search_fields = ['id', 'name', 'description', 'parameters', 'updated_data', 'created_data']
    list_editable = ['name', 'description', 'parameters']

    class Meta:
        model = GeneralSetting
