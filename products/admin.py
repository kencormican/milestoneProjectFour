from django.contrib import admin

from .models import Product
from categories.models import Category, Subcategory


# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'category',
        'subcategory',
        'name',
        'price',
        'quantity',
        'image1',
        'image2',
    )

    # sort order by primary key
    ordering = ('pk',)


admin.site.register(Product, ProductAdmin)
