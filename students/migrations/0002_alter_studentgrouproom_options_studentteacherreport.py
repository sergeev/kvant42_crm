# Generated by Django 4.0.5 on 2023-03-24 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0005_alter_staff_staff_photo_alter_teacher_kvantum'),
        ('kvantums', '0003_alter_kvantum_options_kvantum_program_doc'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentgrouproom',
            options={'verbose_name': 'Ученик(а)', 'verbose_name_plural': 'Состав группы'},
        ),
        migrations.CreateModel(
            name='StudentTeacherReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(help_text='Группа 4', max_length=100, null=True, verbose_name='Группа')),
                ('report_date', models.DateField(verbose_name='Дата отчета')),
                ('group_time_start', models.TimeField(verbose_name='Начало занятия')),
                ('group_time_end', models.TimeField(verbose_name='Конец занятия')),
                ('arrows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvantums.kvantum', verbose_name='Направление')),
                ('teacher', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='personals.teacher', verbose_name='Выберите преподавателя')),
            ],
            options={
                'verbose_name': 'Всего отчетов',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]
