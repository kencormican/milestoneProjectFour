from django.shortcuts import render


# Create your views here.

def about(request):
    """ This view returns the about page """
    return render(request, 'about/about.html')
