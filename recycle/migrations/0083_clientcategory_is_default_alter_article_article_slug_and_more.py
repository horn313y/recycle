# Generated by Django 5.1.1 on 2024-10-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0082_client_client_opt_alter_article_article_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcategory',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='По умолчинию присваивать всем новым клиентам'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2024-10-25 13:29:02.984116', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2024-10-25 13:29:02.983611', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2024-10-25 13:29:02.984116', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2024-10-25 13:29:02.984116', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_slug',
            field=models.CharField(default='article2024-10-25 13:29:02.985121', max_length=200, verbose_name='URL'),
        ),
    ]
