# Generated by Django 3.2.4 on 2024-02-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0068_auto_20240221_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweet_type',
            field=models.CharField(blank=True, choices=[('Новость', 'Новость'), ('Выезд', 'Выезд')], default='Новость', max_length=10, verbose_name='Тип заметки'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2024-02-21 12:14:39.730934', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2024-02-21 12:14:39.707403', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2024-02-21 12:14:39.730440', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2024-02-21 12:14:39.731349', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_slug',
            field=models.CharField(default='article2024-02-21 12:14:39.732676', max_length=200, verbose_name='URL'),
        ),
    ]
