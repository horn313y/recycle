# Generated by Django 3.2.4 on 2021-07-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0010_auto_20210705_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug', max_length=200, verbose_name='URL'),
        ),
    ]
