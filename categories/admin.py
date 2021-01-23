from django.contrib import admin
from .models import Category, Subcategory


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'friendly_name',
        'name',
    )

    ordering = ('pk',)


class SubcategoryAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'friendly_name',
        'name',
        'new'
    )

    ordering = ('pk',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
