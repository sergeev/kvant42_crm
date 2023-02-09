from django.db import models


class PortalSettings(models.Model):
    portal_base_href = models.CharField(max_length=400, verbose_name="ссылка на сайт (корневая)")
    portal_title = models.CharField(max_length=400, verbose_name="Название портала")
    portal_keywords = models.CharField(max_length=1000, verbose_name="Ключевые слова")
    portal_description = models.CharField(max_length=1000, verbose_name="")

    class Meta:
        verbose_name = "Настройки портала"
        verbose_name_plural = "Настройки портала"

    def __str__(self):
        return self.portal_title