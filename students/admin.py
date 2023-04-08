from django.contrib import admin

from .models import StudentRang, Student, StudentGroup, StudentGroupRoom, StudentShoolName, StudentTeacherReport
from django.utils.html import format_html
#from advanced_filters.admin import AdminAdvancedFiltersMixin
from students.models import StudentTeacherReport
from django.urls import reverse


class StudentGroupRoomInline(admin.StackedInline):
    model = StudentGroupRoom
    extra = 2


@admin.register(StudentGroup)
class StudentGroupList(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['teacher']}),
        (None, {'fields': ['group_name']}),
        (None, {'fields': ['group_time_start']}),
        (None, {'fields': ['group_time_end']}),
        ('Направление', {'fields': ['arrows'], 'classes': ['collapse']}),
    ]

    # состав группы
    #inlines = [StudentGroupRoomInline]
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


@admin.register(StudentTeacherReport)
class StudentTeacherReport(admin.ModelAdmin):
    # https://django-tips.avilpage.com/en/latest/admin_better_defaults.html
    #actions = ('make_books_available',)

    list_display = ('id', 'name_colored', 'group_name', 'arrows', 'count_students', 'report_date', 'fact_date_report', 'student_checked')

    search_fields = ['teacher']

    list_filter = ['student_checked', 'report_date']
    #advanced_filter_fields = ('teacher', 'report_date', 'fact_date_report', 'student_checked')

    # отображать последние записи
    date_hierarchy = 'fact_date_report'

    list_per_page = 10
    #readonly_fields = ['group_name']

    list_editable = ['student_checked']

    # При добавлении этого функционала происходит удаление данных! Не использовать на боевом сервере!
    # def delete(self, obj):
    #     view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
    #     link = reverse(view_name, args=[students.pk])
    #     html = '<input type="button" onclick="location.href=\'{}\'" value="Delete" />'.format(link)
    #     return format_html(html)

    def name_colored(self, obj):
        if obj.student_checked:
            color_code = '00FF00'
        else:
            color_code = 'FF0000'
        html = '<span style="color: #{};">{}</span>'.format(color_code, obj.teacher)
        return format_html(html)

    name_colored.admin_order_field = 'teacher'
    name_colored.short_description = 'Красным (новый отчет)'

    # def make_books_available(self, modeladmin, request, queryset):
    #     queryset.update(student_checked=True)
    # make_books_available.short_description = "Mark selected books as available"

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''