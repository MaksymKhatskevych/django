from django.db import models


class Information(models.Model):
	'''Модель информации об авторе'''
	title = models.CharField(max_length=70, default='Моя биография')
	image_info = models.ImageField(upload_to='static/img/news')
	description  = models.TextField(verbose_name='Информация обо мне')

	def __str__(self):
		return self.title

# Create your models here.
		