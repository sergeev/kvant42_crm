from django.contrib import admin

from .models import Teacher, Organization, Event, Staff, StaffQualificationGroup


@admin.register(StaffQualificationGroup)
class StaffQualificationGroupList(admin.ModelAdmin):
    #list_display = ('', 'organization_name')

    class META:
        verbose_name = 'Квалификационная группа (персонал)'
        verbose_name_plural = 'Квалификационная группа (персонал)'


@admin.register(Staff)
class StaffList(admin.ModelAdmin):
    list_display = ('account_id', 'organization')

    class META:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'


@admin.register(Event)
class EventList(admin.ModelAdmin):
    list_display = ('staff_id', 'events_name')

    class META:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'


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
