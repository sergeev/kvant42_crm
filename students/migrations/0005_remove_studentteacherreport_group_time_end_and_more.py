# Generated by Django 4.0.5 on 2023-03-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_studentteacherreport_fact_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentteacherreport',
            name='group_time_end',
        ),
        migrations.RemoveField(
            model_name='studentteacherreport',
            name='group_time_start',
        ),
        migrations.AddField(
            model_name='studentteacherreport',
            name='count_students',
            field=models.CharField(default=1, help_text='Введите количество учеников что были на уроке', max_length=10, verbose_name='Учеников было'),
            preserve_default=False,
        ),
    ]
