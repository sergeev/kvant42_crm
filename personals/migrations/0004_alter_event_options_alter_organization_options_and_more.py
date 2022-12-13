# Generated by Django 4.0.5 on 2022-12-13 10:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0003_alter_staff_staff_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'Организацию', 'verbose_name_plural': 'Организации'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Сотрудника', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='staffqualificationgroup',
            options={'verbose_name': 'Квалификационную группу (персонал)', 'verbose_name_plural': 'Квалификационная группа (персонал)'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Преподавателя', 'verbose_name_plural': 'Преподаватели'},
        ),
        migrations.AlterField(
            model_name='event',
            name='events_concurs_name',
            field=models.TextField(help_text='Введите название конкурсного мероприятия', max_length=400, verbose_name='Название конкурсного мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='events_name',
            field=models.TextField(help_text='Введите название мероприятия', max_length=400, verbose_name='Название мероприятия'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='end_work',
            field=models.DateField(blank=True, help_text='Выберите дату окончания трудовой деятельности', null=True, verbose_name='Дата окончания трудовой деятельности'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='passport_series',
            field=models.CharField(blank=True, help_text='Введите вашу серию паспорта 00 ОТСТУП 00', max_length=100, null=True, validators=[django.core.validators.RegexValidator(message="Вы должны ввести не более четырех(4) цифр серии вашего паспорта'", regex='^([0-9]{2}\\s{1}[0-9]{2})?$')], verbose_name='Серия паспорта'),
        ),
    ]