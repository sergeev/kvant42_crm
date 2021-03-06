# Generated by Django 4.0.5 on 2022-06-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kvantum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('name', models.CharField(max_length=200, verbose_name='Название направления')),
                ('description', models.CharField(max_length=1500, verbose_name='Описание направления')),
                ('description_full', models.CharField(max_length=5500, verbose_name='Описание направления - полное')),
                ('age', models.CharField(max_length=10, verbose_name='Возраст')),
                ('group_max', models.CharField(max_length=20, verbose_name='Участников в группе')),
                ('total_hours', models.CharField(max_length=20, verbose_name='Часов учебной программы')),
            ],
            options={
                'verbose_name_plural': 'Квантумы',
            },
        ),
    ]
