from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Product
from categories.models import Category, Subcategory

from .forms import ProductForm


# Create your views here.

def products(request):
    """ This view renders the products pages and associated
    filtering/searching functionality. It will ultimately allow
    editing and deletion of the products by the admin"""

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


@login_required
def add_product(request):
    """ This view renders the add product template and allows
    submission of the ProductForm when action is POST"""

    if not request.user.is_superuser:
        messages.error(
            request, """Apologies, this functionality is only avialble to
            store administrators"""
            )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f"""
                You've Successfully added the {product.name} Product"""
                )
            return redirect(reverse('product_detail', args=[product.id]))
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


@login_required
def edit_product(request, product_id):
    """ This view renders the edit product template and allows
    the update of the product on POST"""

    if not request.user.is_superuser:
        messages.error(
            request, """Apologies, this functionality is only avialble to
            store administrators"""
            )
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"You've Successfully updated {product.name}")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, "Update Product Failed. Please check form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ This view deletes a product from the database"""

    if not request.user.is_superuser:
        messages.error(
            request, """Apologies, this functionality is only avialble to
            store administrators"""
            )
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    current_product = product.name
    product.delete()
    messages.success(request, f"""
    The {current_product} product has been deleted from the database!"""
                     )
    return redirect(reverse('products'))
