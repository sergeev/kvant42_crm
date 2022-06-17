from django.contrib import admin

from .models import Teacher, Organization


@admin.register(Teacher)
class TeacherList(admin.ModelAdmin):
    list_display = ('teacher_full_name', 'kvantum', 'organization_show')

    class META:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'


@admin.register(Organization)
class OrganizationList(admin.ModelAdmin):
    list_display = ('id', 'organization_name')

    class META:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
