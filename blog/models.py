import datetime
from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


  

class Article(models.Model):
    title = models.CharField('Название статьи', max_length=300)
    text = CKEditor5Field('Текст статьи', config_name='extends')
    image = models.ImageField('Изображение', upload_to='media/blog/')
    pub_date = models.DateTimeField('Дата публикации', auto_now=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Автор комментария', max_length=50)
    comment_text = models.TextField('Текст комментария', max_length=500)
    pub_date = models.DateTimeField('Дата публикации', auto_now=True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
