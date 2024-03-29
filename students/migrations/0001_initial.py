# Generated by Django 4.0.5 on 2023-03-22 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personals', '0005_alter_staff_staff_photo_alter_teacher_kvantum'),
        ('kvantums', '0003_alter_kvantum_options_kvantum_program_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_photo', models.ImageField(default='', upload_to='images', verbose_name='Фотография студента')),
                ('certificate', models.CharField(max_length=200, verbose_name='Сертификат ученика')),
                ('name_ot', models.CharField(max_length=200, verbose_name='Имя и Отчество')),
                ('name_fam', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('email_link', models.EmailField(max_length=254, null=True, verbose_name='Email ученика')),
                ('child_date_input', models.DateField(verbose_name='День рождения')),
                ('gender', models.CharField(choices=[('', 'Выберите вариант'), ('Девочка', 'Девочка'), ('Мальчик', 'Мальчик')], default='def', max_length=10, verbose_name='Пол')),
                ('room', models.CharField(max_length=200, verbose_name='Класс')),
                ('inputs_name_legal_representative', models.CharField(max_length=500, verbose_name='Ф.И.О и данные законного представителя ребенка(ученика)')),
                ('name_legal_representativeTelephone', models.CharField(max_length=500, verbose_name='Телефон для связи законного представителя ребенка(ученика)')),
                ('comments', models.TextField(max_length=1000, verbose_name='Комментарии к ученику')),
                ('exp', models.CharField(default=0, max_length=1000, verbose_name='Опыт ученика(Для внутреннего магазина)')),
                ('coin', models.CharField(default=0, max_length=1000, verbose_name='Монеты ученика(Для внутреннего магазина)')),
                ('student_checked', models.BooleanField(default=False, verbose_name='Ученик проверен')),
                ('student_deleted', models.BooleanField(default=False, verbose_name='Ученик не активен(Выпускник)')),
                ('kvantum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvantums.kvantum', verbose_name='Направление')),
                ('organization_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personals.organization', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Студента',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(help_text='Группа 4', max_length=100, null=True, verbose_name='Группа')),
                ('group_time_start', models.TimeField(verbose_name='Начало занятия')),
                ('group_time_end', models.TimeField(verbose_name='Конец занятия')),
                ('arrows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvantums.kvantum', verbose_name='Направление')),
                ('teacher', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='personals.teacher', verbose_name='Выберите преподавателя')),
            ],
            options={
                'verbose_name': 'Всего групп',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='StudentRang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang', models.CharField(max_length=200, verbose_name='Ранг ученика')),
            ],
            options={
                'verbose_name': 'Ранг ученика',
                'verbose_name_plural': 'Ранг ученика',
            },
        ),
        migrations.CreateModel(
            name='StudentShoolName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shool_name', models.CharField(max_length=200, verbose_name='Введите название школы')),
            ],
            options={
                'verbose_name': 'Название школы',
                'verbose_name_plural': 'Название школы',
            },
        ),
        migrations.CreateModel(
            name='StudentGroupRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('student_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentgroup')),
            ],
            options={
                'verbose_name': 'Ученики в группе',
                'verbose_name_plural': 'Состав учеников группы',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='rang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentrang', verbose_name='Ранг ученика'),
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='students.studentshoolname', verbose_name='Школа'),
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personals.teacher', verbose_name='Преподаватель'),
        ),
    ]
