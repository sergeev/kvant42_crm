from django.db import models


class Kvantum(models.Model):
    image = models.ImageField(upload_to='images', verbose_name="Изображение")
    name = models.CharField(max_length=200, verbose_name='Название направления')
    description = models.TextField(max_length=1500, verbose_name="Описание направления")
    description_full = models.TextField(max_length=5500, verbose_name="Описание направления - полное")
    age = models.CharField(max_length=10, verbose_name="Возраст")
    group_max = models.CharField(max_length=20, verbose_name="Участников в группе")
    total_hours = models.CharField(max_length=20, verbose_name="Часов учебной программы")
    program_doc = models.FileField(upload_to='files', verbose_name="Учебная программа PDF", default="none")

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/arrows/%i" % self.id