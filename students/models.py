from django.contrib import admin
from django.db import models
from personals.models import Organization, Teacher
from kvantums.models import Kvantum


class StudentRang(models.Model):
    rang = models.CharField(max_length=200, verbose_name="Ранг ученика")

    class Meta:
        verbose_name = "Ранг ученика"
        verbose_name_plural = "Ранг ученика"

    def __str__(self):
        return self.rang


class StudentShoolName(models.Model):
    shool_name = models.CharField(max_length=200, verbose_name="Введите название школы")

    class Meta:
        verbose_name = "Название школы"
        verbose_name_plural = "Название школы"

    def __str__(self):
        return self.shool_name


class Student(models.Model):
    GENDER = (
        ('', 'Выберите вариант'),
        ('Девочка', 'Девочка'),
        ('Мальчик', 'Мальчик'),
    )
    organization_show = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Организация")
    certificate = models.CharField(max_length=200, verbose_name="Сертификат ученика")
    name_ot = models.CharField(max_length=200, verbose_name="Имя и Отчество")
    name_fam = models.CharField(max_length=200, verbose_name="Фамилия")
    email_link = models.EmailField(blank=False, null=True, verbose_name="Email ученика")
    child_date_input = models.DateField('День рождения')
    gender = models.CharField(max_length=10, choices=GENDER, default='def', verbose_name='Пол')
    school = models.ForeignKey(StudentShoolName, on_delete=models.CASCADE, max_length=200, verbose_name="Школа")
    room = models.CharField(max_length=200, verbose_name="Класс")
    kvantum = models.ForeignKey(Kvantum, on_delete=models.CASCADE, verbose_name="Направление") # Бывший Квантумы:
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")
    inputs_name_legal_representative = models.CharField(max_length=500, verbose_name="Ф.И.О и данные законного представителя ребенка(ученика)")
    name_legal_representativeTelephone = models.CharField(max_length=500, verbose_name="Телефон для связи законного представителя ребенка(ученика)")
    comments = models.TextField(max_length=1000, verbose_name="Комментарии к ученику")
    rang = models.ForeignKey(StudentRang, on_delete=models.CASCADE, verbose_name="Ранг ученика")
    exp = models.CharField(max_length=1000, default=0, verbose_name="Опыт ученика(Для внетреннего магазина)")
    coin = models.CharField(max_length=1000, default=0, verbose_name="Монеты ученика(Для внетреннего магазина)")
    student_checked = models.BooleanField(default=False, verbose_name="Ученик проверен")
    student_deleted = models.BooleanField(default=False, verbose_name="Ученик не активен(Выпускник)")

    class Meta:
        verbose_name = "Студента"
        verbose_name_plural = "Студенты"

    def __unicode__(self):
        return self.certificate

    def __str__(self):
        return self.certificate


class StudentGroup(models.Model):
    teacher = models.ForeignKey(Teacher, default=None, on_delete=models.CASCADE, verbose_name="Выберите преподавателя")
    group_name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Группа", help_text='Группа 4')
    arrows = models.ForeignKey(Kvantum, on_delete=models.CASCADE, verbose_name="Направление")
    group_time = models.TimeField(verbose_name="Учебное время группы")

    class Meta:
        verbose_name = "Всего групп"
        verbose_name_plural = "Группы"

    def __str__(self):
        return "{} - {}".format(self.group_name.__str__(), self.teacher.__str__())


class StudentGroupRoom(models.Model):
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Группу студента"
        verbose_name_plural = "Группы студента"

    def __str__(self):
        return "{}".format(self.student.__str__())



