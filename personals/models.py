from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.html import mark_safe
from django.conf import settings
from django.db import models
from kvantums.models import Kvantum


class Organization(models.Model):
    organization_name = models.CharField(max_length=200, verbose_name="Организация")

    class Meta:
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.organization_name


class StaffQualificationGroup(models.Model):
    qualification_group = models.CharField(max_length=100, verbose_name="Квалификационная группа")

    class Meta:
        verbose_name_plural = "Квалификационная группа (персонал)"

    def __str__(self):
        return self.qualification_group


def staff_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / staff_<id>/<filename>
    return 'staff_{0}/{1}'.format(instance.staff.id, filename)


class Staff(models.Model):

    '''
    # creating a validator function
def validate_geeks_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")


# Create your models here.
class GeeksModel(models.Model):
    geeks_mail = models.CharField(
                         max_length = 200,
                         validators =[validate_geeks_mail]
                         )
    '''

    passport_01_regex_validator = [RegexValidator(
        # Регулярное выражение для проверки серии паспорта:
        regex=r'^([0-9]{2}\s{1}[0-9]{2})?$',
        message="Вы должны ввести не более четырех(4) цифр серии вашего паспорта'")]

    passport_02_regex_validator = [RegexValidator(
        # Регулярное выражение для проверки номера паспорта:
        regex=r'^([0-9]{6})?$',
        message="Вы должны ввести не более шести(6) цифр номера вашего паспорта'")]

    GENDER_STAFF = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )

    APPLICATION_PYTE = (
        ('Соискатель', 'Соискатель'),
        ('Аспирант', 'Аспирант'),
    )

    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")

    account_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name="Выберите пользователя из базы(Преподавателя)", error_messages={"unique":"Выберите пользователя из базы"})
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,  help_text='Выберите организацию', verbose_name="Организация")
    staff_photo = models.ImageField(upload_to='images/staff/photo/', verbose_name="Фотография работника")
    first_name = models.CharField(max_length=300, help_text='Введите ваше имя', verbose_name="Имя")
    surname = models.CharField(max_length=300, help_text='Введите вашу фамилию', verbose_name="Фамилия")
    patronymic = models.CharField(max_length=300, help_text='Введите ваше отчество', verbose_name="Отчество")
    gender = models.CharField(max_length=30, choices=GENDER_STAFF, verbose_name="Пол")
    data_of_birth = models.DateField(null=True, help_text="Выберите вашу дату рождения", verbose_name="Дата рождения")
    home_address = models.CharField(max_length=500, null=True, help_text='Введите ваш домашний адрес', verbose_name="Домашинй адрес")
    email_address_0 = models.EmailField(max_length=256, null=True, help_text='Введите вашу электронную почту', verbose_name="Почтовый ящик")
    email_address_1 = models.EmailField(max_length=256, null=True, help_text='Введите вашу дополнительную почту', verbose_name="Почтовый ящик(дополнительный")
    email_address_2 = models.EmailField(max_length=256, null=True, help_text='Введите еще один дополнительную почту', verbose_name="Почтовый ящик(дополнительный")
    telephone_mobile = models.CharField(null=True, validators=[phoneNumberRegex], max_length=16, unique=True, help_text='Введит ваш мобильный телефон', verbose_name="Мобильный телефон")
    telephone_home = models.CharField(null=True, validators=[phoneNumberRegex], max_length=16, unique=True, help_text='Введите ваш домашний номер телефона', verbose_name="Домашний телефон")
    telephone_relative = models.CharField(null=True, validators=[phoneNumberRegex], max_length=16, unique=True, help_text='Введите контактный номер телефона вашего родственника', verbose_name="Телефон родственника")
    time_standard = models.CharField(max_length=100,  help_text='Введите табельный номер', verbose_name="Табельный номер")
    qualification_group = models.ForeignKey(StaffQualificationGroup, on_delete=models.CASCADE, help_text='Введите квалификационную группу работника', verbose_name="Квалификационная группа")
    applicant_student = models.CharField(max_length=30, choices=APPLICATION_PYTE, help_text='Выберите из вариантов', verbose_name="Соискатель / Аспирант")
    start_work = models.DateField(null=True, help_text='Выберите дату начала трудовой деятельности', verbose_name="Дата начала трудовой деятельности")
    end_work = models.DateField(null=True, help_text='Выберите дату окончания трудовой деятельности', verbose_name="Дата окончания трудовой деятельности")
    underemployment = models.BooleanField(default=False, help_text='Выберите тип занятости', verbose_name='Неполная занятость(Да или нет)по умлочанию - НЕТ')
    retiree = models.BooleanField(default=False, help_text='Выберите один из вариантов', verbose_name='Пенсионер по выслуге лет, по умлочанию - НЕТ')
    inn = models.CharField(max_length=100, null=True, help_text='Введите ваш ИНН', verbose_name="ИНН")
    snils = models.CharField(max_length=100, null=True, help_text='введите ваш СНИЛС', verbose_name="СНИЛС")
    passport_series = models.CharField(max_length=100, blank=True, null=True, validators=passport_01_regex_validator, help_text='Введите вашу серию паспорта 00 ОТСТУП 00',  verbose_name='Серия паспорта')
    passport_number = models.CharField(max_length=100, blank=True, null=True, validators=passport_02_regex_validator, help_text='Выберите ваш номер паспорта 000000',  verbose_name='Номер паспорта')
    passport_issued_by = models.CharField(max_length=600, blank=True, null=True, help_text='Кем выдан паспорт УФМС / МВД',  verbose_name='Кем выдан паспорт УФМС / МВД')
    passport_date_of_issue = models.DateField(blank=True, null=True, help_text='Дата выдачи',  verbose_name='Дата выдачи')
    policy_series = models.CharField(max_length=256, blank=True, null=True, help_text='Введите серию полиса',  verbose_name='Серия полиса')
    policy_number = models.CharField(max_length=256, blank=True, null=True, help_text='Введите номер полеса',  verbose_name='Номер полиса')
    policy_date_of_issue = models.DateField(blank=True, null=True, help_text='Введите дату выдачи полеса',  verbose_name='Дата выдачи полиса')
    policy_insured_company = models.CharField(max_length=256, blank=True, null=True, help_text='Введите компанию страхователя',  verbose_name='Компания страхователь')

    def image_tag(self):
        if self.staff_photo != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.staff_photo))

    class META:
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.patronymic}'


class Teacher(models.Model):
    teacher_full_name = models.ForeignKey(Staff, default=None, on_delete=models.CASCADE, verbose_name="Выберите пользователя из базы(Преподавателя)")
    kvantum = models.ForeignKey(Kvantum, on_delete=models.CASCADE, verbose_name="Квантум")
    organization_show = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Организация")
    images = models.ImageField(upload_to='images/teachers', verbose_name="Изображение")
    link_web_main = models.URLField(max_length=200, blank=True, null=True,  verbose_name="Ссылка на персональную страниц")
    link_web_facebook = models.URLField(max_length=500, blank=True, null=True,  verbose_name="Ссылка на страницу FaceBook")
    link_web_twitter = models.URLField(max_length=500, blank=True, null=True,  verbose_name="Ссылка на страницу Twitter")
    link_web_skype = models.URLField(max_length=500, blank=True, null=True,  verbose_name="Ссылка на страницу Skype")
    link_web_google = models.URLField(max_length=500, blank=True, null=True,  verbose_name="Ссылка на страницу Google")
    link_web_vk = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на страницу VK")
    teacher_desc = models.CharField(max_length=500, blank=True, null=True,  verbose_name="Описание, образоваине и т.д")

    class Meta:
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return "{}".format(self.teacher_full_name.__str__())


class Event(models.Model):

    EVENT_NAMES_CHOICES = (
        ('event_0', 'Выставка'),
        ('event_1', 'Конкурс'),
        ('event_2', 'Конференция'),
        ('event_3', 'Мастер-класс'),
        ('event_4', 'Семинар'),
    )

    EVENT_STATUS_CHOICES = (
        ('event_status_0', 'Победитель'),
        ('event_status_1', 'Лауреат'),
        ('event_status_2', 'Участник'),
    )

    EVENT_FORM_CHOICES = (
        ('event_form_0', 'Очно'),
        ('event_form_1', 'Заочно'),
    )

    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, help_text='Выберите педагога из списка',  verbose_name='Педагог')
    events_name = models.CharField(max_length=400, help_text='Введите название мероприятия', verbose_name='Название мероприятия')
    # Выставка / Конкурс / Конференция / Мастер-класс / Семинар
    events_name_show = models.CharField(max_length=50, choices=EVENT_NAMES_CHOICES, help_text='Выберите вид мероприятия',  verbose_name='Вид мероприятия')
    events_level = models.CharField(max_length=50, choices=EVENT_NAMES_CHOICES, help_text='Выберите уровень проведения',  verbose_name='Уровень проведения')
    events_form = models.CharField(max_length=50, choices=EVENT_FORM_CHOICES, help_text='Выберите форму участия',  verbose_name='Форма участия')
    events_status = models.CharField(max_length=50, choices=EVENT_STATUS_CHOICES, help_text='Выберите статус участия',  verbose_name='Статус участия')
    events_concurs_name = models.CharField(max_length=400, help_text='Введите название конкурсного мероприятия',  verbose_name='Название конкурсного мероприятия')
    events_participation_year = models.DateField(blank=True, null=True, help_text='Введите год участия',  verbose_name='Год участия')

    def __str__(self):
        return self.events_name

    class Meta:
        verbose_name_plural = "Мероприятия"
