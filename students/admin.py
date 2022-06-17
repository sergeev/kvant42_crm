from django.contrib import admin

from .models import StudentRang, Student, StudentGroup, StudentGroupRoom


class StudentGroupRoomInline(admin.StackedInline):
    model = StudentGroupRoom
    extra = 3


@admin.register(StudentGroup)
class StudentGroupList(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['teacher']}),
        (None, {'fields': ['group_time']}),
        ('Направление', {'fields': ['arrows'], 'classes': ['collapse']}),
    ]
    inlines = [StudentGroupRoomInline]


@admin.register(StudentRang)
class StudentRangList(admin.ModelAdmin):
    list_display = ('id', 'rang')

    class META:
        verbose_name = 'Ранги учеников'
        verbose_name_plural = 'Ранги учеников'


@admin.register(Student)
class StudentList(admin.ModelAdmin):
    list_display = ('certificate', 'rang')

    class META:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'