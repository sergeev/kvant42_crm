# Generated by Django 4.0.5 on 2023-02-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvantums', '0002_alter_kvantum_options_alter_kvantum_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kvantum',
            options={'verbose_name': 'Направление', 'verbose_name_plural': 'Направления'},
        ),
        migrations.AddField(
            model_name='kvantum',
            name='program_doc',
            field=models.FileField(default='none', upload_to='files', verbose_name='Учебная программа PDF'),
        ),
    ]
