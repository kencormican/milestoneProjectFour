from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# from categories.models import Category, Subcategory
from .models import Product


# Create your views here.

def products(request):
    """ This view renders the products pages and will ultimately
    allow editing and deletion of the products in by the admin"""

    products = Product.objects.all()

    for product in products:
        product.name = product.name.lower()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ This view renders a product's detailed information & will
    ultimately allow editing and deletion of the product by the admin"""

    product = get_object_or_404(Product, pk=product_id)
    product.name = product.name.lower()
    product.summary = product.summary.lower()
    product.detail = product.summary.lower()

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
