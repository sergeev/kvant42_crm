# Generated by Django 4.0.5 on 2022-06-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0002_alter_staff_passport_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_photo',
            field=models.ImageField(upload_to='images/staff/photo/', verbose_name='Фотография работника'),
        ),
    ]
