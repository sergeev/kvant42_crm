# Generated by Django 4.0.5 on 2023-02-09 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kvantums', '0003_alter_kvantum_options_kvantum_program_doc'),
        ('students', '0003_studentshoolname_alter_studentgroup_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_photo',
            field=models.ImageField(default='', upload_to='images', verbose_name='Фотография студента'),
        ),
        migrations.AlterField(
            model_name='student',
            name='kvantum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvantums.kvantum', verbose_name='Направление'),
        ),
    ]
