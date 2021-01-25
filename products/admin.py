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
    )

    ordering = ('pk',)


admin.site.register(Product, ProductAdmin)
