from django.shortcuts import render
from django.contrib import messages

# from categories.models import Category, Subcategory
from .models import Product


# Create your views here.

def products(request):
    """ This view renders the products pages and allow will
    ultimately allow editing and deletion of the products in
    by the admin"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

