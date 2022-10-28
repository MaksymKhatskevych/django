from django.db import models


class Contact(models.Model):
	'''Модель контактов'''
	phone = models.CharField(max_length=12)
	email = models.EmailField()
	telega_link = models.CharField(max_length=120)
	facebook_link = models.CharField(max_length=120)
	instagram_link = models.CharField(max_length=120)

	def __str__(self):
		return self.phone
# Create your models here.
