# Generated by Django 5.1.1 on 2024-10-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0083_clientcategory_is_default_alter_article_article_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='gid',
            field=models.CharField(blank=True, max_length=200, verbose_name='Gid'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2024-10-26 22:04:03.147095', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2024-10-26 22:04:03.146095', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2024-10-26 22:04:03.146095', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2024-10-26 22:04:03.147095', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_slug',
            field=models.CharField(default='article2024-10-26 22:04:03.148095', max_length=200, verbose_name='URL'),
        ),
    ]
