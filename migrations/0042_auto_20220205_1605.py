# Generated by Django 3.2.4 on 2022-02-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0041_auto_20220203_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2022-02-05 16:05:06.980356', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2022-02-05 16:05:06.901899', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2022-02-05 16:05:06.981058', max_length=200, verbose_name='URL'),
        ),
    ]
