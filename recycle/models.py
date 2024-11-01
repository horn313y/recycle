import datetime
from django.urls import reverse
from django.db import models
from django_editorjs_fields import EditorJsJSONField, EditorJsTextField

from django.contrib.auth.models import User

PURCACHE_CHOICES = (
    ('Килограмм','кг'),
    ('Штук', 'шт')
)

TWEET_CHOICES = (
    ('Новость','Новость'),
    ('Выезд', 'Выезд'),
    ('Внимание', 'Внимание'),
)


class Category(models.Model):
    cat_name = models.CharField('Название категории продукта', max_length=200)
    cat_title = models.CharField('Заголовок для Open Graph (og:title)', max_length=200, blank=True)
    cat_metadesc = models.CharField('Описание для Open Graph (og:description)', max_length=300, blank=True)
    cat_slug = models.CharField('URL', max_length=200, default='slug' + str(datetime.datetime.now()))
    cat_short_desc = models.TextField('Короткое описание', blank=True)
    cat_desc = models.TextField('Полное описание', blank=True)
    cat_image = models.ImageField('Изображение категории', default='placeholder.jpg')
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    cat_question_1 = models.TextField('Вопрос 1', blank=True, default='')
    cat_answer_1 = EditorJsJSONField(blank=True,  default='')
    cat_question_2 = models.TextField('Вопорос 2', blank=True, default='')
    cat_answer_2 = EditorJsJSONField(blank=True, default='')
    cat_question_3 = models.TextField('Вопрос 3', blank=True, default='')
    cat_answer_3=EditorJsJSONField(blank=True, default='')
    cat_question_4 = models.TextField('Вопрос 4', blank=True, default='')
    cat_answer_4=EditorJsJSONField(blank=True, default='')
    cat_question_5 = models.TextField('Вопрос 5', blank=True, default='')
    cat_answer_5=EditorJsJSONField(blank=True, default='')
    

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('products', args=[self.cat_slug])

class Product(models.Model):
    product_name = models.CharField('Название продукта', max_length=200)
    product_title = models.CharField('Заголовок для Open Graph (og:title)', max_length=200)
    product_metadesc = models.CharField('Описание для Open Graph (og:description)', max_length=300)
    color = models.CharField('Оплата', max_length=10, choices=PURCACHE_CHOICES, default='kg')
    product_price = models.CharField('Цена', max_length=200, blank=True, null=True)
    product_short_desc = models.TextField('Короткое описание', blank=True)
    product_desc = models.TextField('Артикул', blank=True)
    product_image = models.ImageField('Изображение продукта', default='placeholder.jpg')
    product_image_big = models.ImageField('Большое изображение продукта', default='placeholder.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    body_editorjs = EditorJsJSONField()
    product_slug = models.CharField('URL', max_length=200, default='product' + str(datetime.datetime.now()))

    def __str__(self):
        return self.product_name
        
    def get_absolute_url(self):
        return reverse('product', args=[self.product_slug])

class Article(models.Model):
    article_name = models.CharField('Заголовок H1', max_length=200)
    article_title = models.CharField('Заголовок для Open Graph (og:title)', max_length=200)
    article_metadesc = models.CharField('Описание для Open Graph (og:description)', max_length=300)
    article_slug = models.CharField('URL', max_length=200, default='article' + str(datetime.datetime.now()))
    article_short_desc = models.TextField('Короткое описание для Schema', blank=True)
    article_image = models.ImageField('Изображение статьи')
    isStock = models.BooleanField(default=False)
    body_editorjs = EditorJsJSONField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.article_name

    def get_absolute_url(self):
        return reverse('article', args=[self.article_slug])

class Region(models.Model):
    region_name = models.CharField('Название региона', max_length=200)
    region_title = models.CharField('Заголовок для Open Graph (og:title)', max_length=200)
    region_metadesc = models.CharField('Описание для Open Graph (og:description)', max_length=300)
    region_slug = models.CharField('URL', max_length=200, default='region' + str(datetime.datetime.now()))
    region_short_desc = models.TextField('Короткое описание', blank=True)
    body_editorjs = EditorJsJSONField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    region_add_info = models.TextField('Доп. информация', blank=True)

    def __str__(self):
        return self.region_name

    def get_absolute_url(self):
        return reverse('region', args=[self.region_slug])


class Punkt(models.Model):
    punkt_name = models.CharField('Название пункта приема', max_length=200)
    punkt_title = models.CharField('Заголовок для Open Graph (og:title)', max_length=200)
    punkt_metadesc = models.CharField('Описание для Open Graph (og:description)', max_length=300)
    punkt_short_desc = models.TextField('Короткое описание', blank=True)
    punkt_geo = models.CharField('Описание description', max_length=300, default="55.659173,37.762848")
    punkt_image = models.ImageField('Изображение пункта')
    body_editorjs = EditorJsJSONField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    punkt_negative = models.IntegerField('Негативный рейтинг', blank=True, default=0)
    punkt_positive = models.IntegerField('Позитивный рейтинг', blank=True, default=0)

    def __str__(self):
        return self.punkt_name


class Agent(models.Model):
    user_link = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    agent_name = models.CharField('Имя агента', max_length=200)
    agent_title = models.CharField('Заголовок для Open Graph (og:title)', max_length=200)
    agent_metadesc = models.CharField('Описание для Open Graph (og:description)', max_length=300)
    agent_short_desc = models.TextField('Короткое описание', blank=True)
    agent_image = models.ImageField('Фото агента')
    body_editorjs = EditorJsJSONField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.agent_name


class Tweet(models.Model):
    tweet_name = models.CharField('Заголовок H1', max_length=200)
    tweet_slug = models.CharField('URL', max_length=200, default='article' + str(datetime.datetime.now()))
    tweet_short_desc = models.TextField('Короткое описание для Schema', blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    tweet_type = models.CharField('Тип заметки', max_length=10, choices=TWEET_CHOICES, blank=True)
    region = models.ManyToManyField(Region, blank=True)
    def __str__(self):
        return self.tweet_name

    def get_absolute_url(self):
        return reverse('tweet', args=[self.tweet_slug])



class ClientSales(models.Model):
    name = models.CharField('Название', max_length=200)
    short_desc = models.TextField('Описание', blank=True)
    price_link = models.CharField('Ссылка на специальный прайс', max_length=200, blank=True)
    
    def __str__(self):
        return self.name

class ClientCategory(models.Model):
    name = models.CharField('Название', max_length=200)
    short_desc = models.TextField('Описание', blank=True)
    sales = models.ManyToManyField(ClientSales, blank=True)
    is_default = models.BooleanField('По умолчинию присваивать всем новым клиентам', default=False)
    def __str__(self):
        return self.name

class Client(models.Model):
    djuser = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Телефон', max_length=200)
    name = models.CharField('Имя', max_length=200)
    client_opt = models.CharField(max_length=6, null=True, blank=True)
    client_category = models.ManyToManyField(ClientCategory, blank=True)
    gid = models.CharField('Gid', max_length=200, blank=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Deal(models.Model):
    client_id = models.CharField('Идентификатор пользователя', max_length=200)
    client_tel = models.CharField('Телефон пользователя', max_length=200)
    agent_id = models.CharField('Идентификатор агента', max_length=200)
    code = models.CharField('Код из СМС', max_length=200)
    pub_date = models.DateTimeField(default=datetime.datetime.now)



    def __str__(self):
        return self.name