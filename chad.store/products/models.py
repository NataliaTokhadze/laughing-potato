from django.db import models
from django.core.validators import MaxValueValidator
from config.model_utils.models import TimeStampedModel
from products.choices import Currency

class Product(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    currency = models.CharField(max_length=255, choices=Currency.choices, default=Currency.GEL)
    quantity = models.PositiveIntegerField()

    def average_rating(self):
        pass


class Review(TimeStampedModel, models.Model):
    product = models.ForeignKey('products.Product', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='reviews', on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])


class FavoriteProduct(TimeStampedModel, models.Model):
    product = models.ForeignKey('products.Product', related_name='favorite_products', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='favorite_products', on_delete=models.SET_NULL, null=True, blank=True)


class ProductTag(TimeStampedModel, models.Model):
    tag_name = models.CharField(max_length=255)   
    products = models.ManyToManyField('products.Product', related_name='products_tags')


class Cart(TimeStampedModel, models.Model):
    products = models.ManyToManyField('products.Product', related_name='carts')
    user = models.OneToOneField('users.User', related_name='cart', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)


class ProductImage(TimeStampedModel, models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('products.Product', related_name='images', on_delete=models.CASCADE)
    