# Generated by Django 3.2.4 on 2022-02-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0040_auto_20220201_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_short_desc',
            field=models.TextField(blank=True, verbose_name='Короткое описание для Schema'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2022-02-03 13:34:56.171411', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2022-02-03 13:34:56.052279', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.TextField(blank=True, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2022-02-03 13:34:56.172142', max_length=200, verbose_name='URL'),
        ),
    ]