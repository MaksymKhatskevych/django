# Generated by Django 2.2.19 on 2022-02-01 13:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210407_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Текст статьи'),
        ),
    ]