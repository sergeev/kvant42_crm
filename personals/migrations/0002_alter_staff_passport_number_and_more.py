# Generated by Django 4.0.5 on 2022-06-19 18:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='passport_number',
            field=models.CharField(blank=True, help_text='Выберите ваш номер паспорта 000000', max_length=100, null=True, validators=[django.core.validators.RegexValidator(message="Вы должны ввести не более шести(6) цифр номера вашего паспорта'", regex='^([0-9]{6})?$')], verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='passport_series',
            field=models.CharField(blank=True, help_text='Введите вашу серию паспорта 00 00', max_length=100, null=True, validators=[django.core.validators.RegexValidator(message="Вы должны ввести не более четырех(4) цифр серии вашего паспорта'", regex='^([0-9]{2}\\s{1}[0-9]{2})?$')], verbose_name='Серия паспорта'),
        ),
    ]