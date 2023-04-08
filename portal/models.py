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


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")