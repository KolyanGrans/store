from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название категории')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание категории')

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')
    image = models.ImageField(upload_to='products_images', blank=True, verbose_name='Изображение товара')
    description = models.TextField(verbose_name='Описание товара')
    short_description = models.CharField(max_length=64, verbose_name='Краткое описание товара', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена товара')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, verbose_name='категория товара')

    def __str__(self):
        return f'{self.name} | {self.category.name}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price
