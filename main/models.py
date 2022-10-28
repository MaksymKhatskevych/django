from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField



class News(models.Model):
	"""Новостная модель"""
	title_news = models.CharField(max_length=70)
	description  = CKEditor5Field('Текст статьи', config_name='extends')
	image_news = models.ImageField(upload_to='static/img/news')
	published = models.DateTimeField(verbose_name='Дата публикации')

	def __str__(self):
		return self.title_news





