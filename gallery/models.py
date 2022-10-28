from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/gallery/')
