from django.db import models
from django.conf import settings

from categories.models import Category, Subcategory

# Create your models here.


class Product(models.Model):

    category = models.ForeignKey('categories.Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('categories.Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    # product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    # category = models.ForeignKey('Category', null=False, blank=False, on_delete=models.CASCADE)
    # subcategory = models.ForeignKey('Subcategory', null=False, blank=False, on_delete=models.CASCADE)

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)

    quantity = models.PositiveIntegerField(
        default=1, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    summary = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    image1_url = models.URLField(max_length=1024, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2_url = models.URLField(max_length=1024, null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
