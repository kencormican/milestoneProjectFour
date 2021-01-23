from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Subcategory

from .forms import SubcategoryForm


# Create your views here.

def manage_categories(request):
    """ This view renders the manage categories page and allow
    editing and deletion of the subcategories in the database """

    subcategories = Subcategory.objects.all()

    context = {
        'subcategories': subcategories,
    }

    return render(request, 'categories/categories.html', context)


def add_subcategory(request):
    """ Add a subcategory to the database """

    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            """ Confirm if category already exists in database
            before saving form input"""
            # cleaned_data() method used to standardise form to dictionary before check.
            input_standardised_to_dict = form.cleaned_data
            dict_input_name = input_standardised_to_dict.get('name')
            if Subcategory.objects.filter(name=dict_input_name).exists():
                print("Category Name already exists. Please define another?")
            else:
                form.save()

            return redirect(reverse('categories'))
    else:
        form = SubcategoryForm()

    template = 'categories/add_subcategory.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_subcategory(request, subcategory_id):
    """ Update a pre-exiting subcategory on the database """

    subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect(reverse('categories'))
    else:
        form = SubcategoryForm(instance=subcategory)

    template = 'categories/edit_subcategory.html'
    context = {
        'form': form,
        'subcategory': subcategory
    }

    return render(request, template, context)


def delete_subcategory(request, subcategory_id):
    """ Delete a subcategory from the database """
    subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
    subcategory.delete()
    print('Category deleted!')
    return redirect(reverse('categories'))
