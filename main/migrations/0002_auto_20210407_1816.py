# Generated by Django 2.2.19 on 2021-04-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_news',
            field=models.ImageField(upload_to='static/img/news'),
        ),
    ]