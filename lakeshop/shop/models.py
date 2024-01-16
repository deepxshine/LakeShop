from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    image = models.ImageField(upload_to='genres/', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Владелец магазина')
    name = models.CharField(max_length=255, verbose_name='Название магазина')
    image = models.ImageField(upload_to='genres/')
    description = models.CharField(max_length=2048, verbose_name='Описание')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Parameter(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    unit = models.CharField(max_length=32, verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.CharField(max_length=2048, verbose_name='Описание')
    old_price = models.PositiveIntegerField(verbose_name='Цена без скидки',
                                            blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    pubdate = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата добавления')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,
                             verbose_name='Магазин')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    tags = models.CharField(max_length=1024, verbose_name='Тэги для поиска')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class ParametersInProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Товар')
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE,
                                  verbose_name='Параметр')
    value = models.CharField(max_length=63, verbose_name='Значение')

    class Meta:
        verbose_name = 'Параметры в товаре'
        verbose_name_plural = 'Параметры в товарах'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Товар')
    image = models.ImageField(upload_to='products/', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Картинка в товаре'
        verbose_name_plural = 'Картинки в товарах'


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Товар', related_name='fav')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь', related_name='fav')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Товар', related_name='cart')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь', related_name='cart')
    count = models.PositiveIntegerField(verbose_name='Количество товара')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
