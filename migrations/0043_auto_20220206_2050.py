# Generated by Django 2.2 on 2022-02-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0042_auto_20220205_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2022-02-06 20:50:38.747381', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2022-02-06 20:50:38.718297', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='punkt',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2022-02-06 20:50:38.748141', max_length=200, verbose_name='URL'),
        ),
    ]
