# Generated by Django 2.2 on 2022-07-20 19:33

from django.db import migrations, models
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0054_auto_20220309_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2022-07-20 19:33:35.916566', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2022-07-20 19:33:35.888552', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='body_editorjs',
            field=django_editorjs_fields.fields.EditorJsJSONField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2022-07-20 19:33:35.915817', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2022-07-20 19:33:35.917248', max_length=200, verbose_name='URL'),
        ),
    ]
