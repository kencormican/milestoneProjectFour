from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Subcategory

from django.contrib import messages

from .forms import AddSubcategoryForm, EditSubcategoryForm


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
        form = AddSubcategoryForm(request.POST)
        if form.is_valid():
            """ Confirm if category or friendly name already exists
            in database before saving form input"""

            """ cleaned_data() method used to standardise form
            to dictionary before check"""
            input_standardised_to_dict = form.cleaned_data
            dict_input_name = input_standardised_to_dict.get('name')
            dict_input_friendly_name = input_standardised_to_dict.get(
                'friendly_name')
            if Subcategory.objects.filter(name=dict_input_name).exists():
                messages.warning(
                    request, "Category already exists. Please choose another"
                )
            elif Subcategory.objects.filter(
                    friendly_name=dict_input_friendly_name).exists():
                if dict_input_friendly_name:
                    messages.warning(
                        request, """Friendly Name already exists.
                        Please choose another"""
                    )
                else:
                    form.save()
                    messages.success(
                        request, "You've Successfully added a new Category"
                    )
                    return redirect(reverse('categories'))
            else:
                form.save()
                messages.success(
                    request, "You've Successfully added a new Category"
                )
                return redirect(reverse('categories'))
        else:
            messages.error(
                request, 'Failed to add category.'
            )
    else:
        form = AddSubcategoryForm()
        messages.info(request, 'You are adding a new category')

    template = 'categories/add_subcategory.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_subcategory(request, subcategory_id):
    """ Update a pre-exiting subcategory on the database """

    subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
    if request.method == 'POST':
        form = EditSubcategoryForm(request.POST, instance=subcategory)
        """Confirm if friendly name already exists in database before saving form
        also allowing friendly name to be updated with Null entry"""
        if form.is_valid():
            input_standardised_to_dict = form.cleaned_data
            dict_input_friendly_name = input_standardised_to_dict.get(
                'friendly_name')
            if Subcategory.objects.filter(
                        friendly_name=dict_input_friendly_name).exists():
                if dict_input_friendly_name:
                    messages.warning(
                        request, f""""{subcategory.friendly_name} already exists.
                        Please choose another"""
                    )
                else:
                    form.save()
                    messages.success(
                        request, f"""You've Successfully
                        updated {subcategory.name}"""
                    )
                    return redirect(reverse('categories'))
            else:
                form.save()
                messages.success(
                    request, f"You've Successfully updated {subcategory.name}"
                )
                return redirect(reverse('categories'))
        else:
            messages.error(
                request, 'Failed to update category.'
            )
    else:
        form = EditSubcategoryForm(instance=subcategory)
        messages.info(request, f'You are editing {subcategory.name}')

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
    messages.success(request, 'Category deleted!')
    return redirect(reverse('categories'))
