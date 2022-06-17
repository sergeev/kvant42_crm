from django.contrib.auth.models import User
from django.db import models
from kvantums.models import Kvantum


class Organization(models.Model):
    organization_name = models.CharField(max_length=200, verbose_name="Организация")

    class Meta:
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.organization_name


class Teacher(models.Model):
    teacher_full_name = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name="Выберите пользователя из базы(Преподавателя)")
    kvantum = models.ForeignKey(Kvantum, on_delete=models.CASCADE, verbose_name="Квантум")
    organization_show = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Организация")
    images = models.ImageField(upload_to='images/teachers', verbose_name="Изображение")
    link_web_main = models.URLField(max_length=200, blank=True, null=True,  verbose_name="Ссылка на персональную страниц")
    link_web_facebook = models.URLField(max_length=500, blank=True, null=True,  verbose_name="Ссылка на страницу FaceBook")
    link_web_twitter = models.URLField(max_length=500, blank=True, null=True,  verbose_name="Ссылка на страницу Twitter")
    link_web_skype = models.URLField(max_length=500, blank=True, null=True,  verbose_name="Ссылка на страницу Skype")
    link_web_google = models.URLField(max_length=500, blank=True, null=True,  verbose_name="Ссылка на страницу Google")
    link_web_vk = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на страницу VK")
    teacher_desc = models.CharField(max_length=500, blank=True, null=True,  verbose_name="Описание, образоваине и т.д")

    class Meta:
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return "{}".format(self.teacher_full_name.__str__())
