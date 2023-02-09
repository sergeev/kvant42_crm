from django.contrib import admin

from .models import StudentRang, Student, StudentGroup, StudentGroupRoom, StudentShoolName


class StudentGroupRoomInline(admin.StackedInline):
    model = StudentGroupRoom
    extra = 2


@admin.register(StudentGroup)
class StudentGroupList(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['teacher']}),
        (None, {'fields': ['group_name']}),
        (None, {'fields': ['group_time']}),
        ('Направление', {'fields': ['arrows'], 'classes': ['collapse']}),
    ]

    # состав группы
    inlines = [StudentGroupRoomInline]


@admin.register(StudentRang)
class StudentRangList(admin.ModelAdmin):
    list_display = ('id', 'rang')

    class Meta:
        verbose_name = 'Ранг ученика'
        verbose_name_plural = 'Ранги учеников'


@admin.register(StudentShoolName)
class StudentShoolName(admin.ModelAdmin):
    list_display = ('id', 'shool_name')

    class Meta:
        verbose_name = 'Школы'
        verbose_name_plural = 'Школы'


@admin.register(Student)
class StudentList(admin.ModelAdmin):
    list_display = ('certificate', 'name_ot', 'name_fam', 'kvantum', 'rang', 'student_checked', 'student_deleted')
    #ordering = ('-create_at',)

    search_fields = ['certificate', 'name_ot', 'name_fam']

    list_filter = ['student_checked']

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'