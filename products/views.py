from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product
from categories.models import Category, Subcategory

from .forms import ProductForm


# Create your views here.

def products(request):
    """ This view renders the products pages and associated
    filtering/searching functionality. It will ultimately allow
    editing and deletion of the products in by the admin"""

    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None

    products = Product.objects.all()

    for product in products:
        product.name = product.name.lower()

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            # not using if sorkey == 'name'

            if sortkey == 'subcategory':
                sortkey = 'subcategory__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory'].split(',')
            products = products.filter(subcategory__name__in=subcategories)
            subcategories = Subcategory.objects.filter(name__in=subcategories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))

            # This provides the or operation against the search criteria
            queries = Q(name__icontains=query) | Q(
                summary__icontains=query) | Q(
                category__name__icontains=query) | Q(
                    subcategory__name__icontains=query)
            products = products.filter(queries)
            messages.success(
                request, "Please see results of your search below!")

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
        'current_sorting': current_sorting,
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


def add_product(request):
    """ This view renders the add product template and allows
    submission of the ProductForm when action is POST"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "You've Successfully added a New Product")
            return redirect(reverse('products'))
        else:
            messages.error(
                request, "Failed to add Product. Please check form is valid."
            )
    else:
        form = ProductForm
        messages.info(request, 'You are adding a new product')

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
