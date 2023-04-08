# Generated by Django 4.0.5 on 2023-03-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortalSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portal_base_href', models.CharField(max_length=400, verbose_name='ссылка на сайт (корневая)')),
                ('portal_title', models.CharField(max_length=400, verbose_name='Название портала')),
                ('portal_keywords', models.CharField(max_length=1000, verbose_name='Ключевые слова')),
                ('portal_description', models.CharField(max_length=1000, verbose_name='')),
            ],
            options={
                'verbose_name': 'Настройки портала',
                'verbose_name_plural': 'Настройки портала',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
            ],
        ),
    ]
