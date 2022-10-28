from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Description(models.Model):
	"""Description for form order"""
	title = models.CharField(max_length=30)
	text = CKEditor5Field('Текст статьи')

	def __str__(self):
		return self.title


