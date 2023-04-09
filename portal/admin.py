from django.contrib import admin
from .models import PortalSettings


@admin.register(PortalSettings)
class PortalSettingsConfig(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки'

