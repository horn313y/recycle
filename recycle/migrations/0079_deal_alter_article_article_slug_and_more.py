# Generated by Django 5.1.1 on 2024-10-23 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0078_alter_article_article_slug_alter_category_cat_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=200, verbose_name='Идентификатор пользователя')),
                ('client_tel', models.CharField(max_length=200, verbose_name='Телефон пользователя')),
                ('agent_id', models.CharField(max_length=200, verbose_name='Идентификатор агента')),
                ('code', models.CharField(max_length=200, verbose_name='Код из СМС')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2024-10-23 13:46:35.242579', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2024-10-23 13:46:35.241579', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2024-10-23 13:46:35.241579', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2024-10-23 13:46:35.242579', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_slug',
            field=models.CharField(default='article2024-10-23 13:46:35.243579', max_length=200, verbose_name='URL'),
        ),
    ]
