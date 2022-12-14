# Generated by Django 2.2.17 on 2021-03-02 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название статьи')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('image', models.ImageField(upload_to='media/blog/', verbose_name='Изображение')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Автор комментария')),
                ('comment_text', models.TextField(max_length=500, verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
