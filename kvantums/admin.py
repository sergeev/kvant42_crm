from django.contrib import admin

from .models import Kvantum


@admin.register(Kvantum)
class KvantumList(admin.ModelAdmin):
    list_display = ('name', 'description', 'age', 'group_max', 'total_hours')

    class Meta:
        verbose_name = 'Квантум'
        verbose_name_plural = 'Квантумы'
