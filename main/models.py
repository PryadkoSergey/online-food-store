from django.db import models
from django.urls import reverse

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length = 20, db_index = True, verbose_name = "Имя")
    time = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Время(мин.)")
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'
    def __str__(self):
        return str(self.status)

class Order(models.Model):
    nameUser = models.CharField(verbose_name='Имя пользователя', max_length=50)
    phone = models.CharField(verbose_name='Номер телефона', max_length = 15)
    readyStatus = models.ForeignKey(Status, verbose_name = "Статус", on_delete = models.PROTECT)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Цена(грн.)")
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплата', default=False)
    IdTelegram =  models.CharField(verbose_name='Id телеграмм', max_length=50, blank=False)

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'
    def __str__(self):
        return str(self.nameUser)

class Category(models.Model):
    name = models.CharField(max_length = 20, db_index = True, verbose_name = "Имя")
    info = models.CharField(max_length = 200, verbose_name = "Описание")
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length = 50, db_index = True, verbose_name = "Имя")
    info = models.CharField(max_length = 200, verbose_name = "Описание")
    category = models.ForeignKey(Category, verbose_name = "Категория", on_delete = models.PROTECT)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Price(грн.)")
    image = models.ImageField(upload_to = 'photos', verbose_name = "Фото продукта")
    show = models.BooleanField(verbose_name='Видимость', default=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return str(self.name)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name = "История", on_delete = models.PROTECT)
    product = models.ForeignKey(Product, verbose_name = "Продукт", on_delete = models.PROTECT)
    class Meta:
        verbose_name = "История-продукт"
        verbose_name_plural = "Истории-Продукты"
    def __str__(self):
        return str(self.order)

class Discounts(models.Model):
    product = models.ForeignKey(Product, verbose_name = "Продукт", on_delete = models.PROTECT)
    percent = models.PositiveIntegerField(verbose_name = "Процент скидки")
    show = models.BooleanField(verbose_name='Оплата', default=True)
    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
    def __str__(self):
        return str(self.product)