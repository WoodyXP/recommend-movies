from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.FloatField()
    brand = models.ForeignKey(Brand, null=False, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Ebay_Product(models.Model):
    title = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)
    price = models.FloatField()
    url = models.TextField()
    seller = models.CharField(max_length=100)

    def __str__(self):
        return self.title