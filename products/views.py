from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product


# Create your views here.

def products(request):
    """ This view renders the products pages and associated
    filtering/seraching functionality. It will ultimately allow
    editing and deletion of the products in by the admin"""

    query = None
    products = Product.objects.all()

    for product in products:
        product.name = product.name.lower()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))

            # This provides the or operation against the search criteria
            queries = Q(name__icontains=query) | Q(summary__icontains=query)
            products = products.filter(queries)
            messages.success(request, "Please see results of your search below!")

    context = {
        'products': products,
        'search_term': query,
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
