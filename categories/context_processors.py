from .models import Subcategory


def add_categories_to_context(request):

    subcategories = Subcategory.objects.all()

    return {
        'subcategories': subcategories,
    }
