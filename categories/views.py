from django.shortcuts import render


# Create your views here.

def categories(request):
    """ This view renders the manage categories page """
    return render(request, 'categories/categories.html')
