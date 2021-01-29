from django.shortcuts import render
from django.contrib import messages


# Create your views here.

def checkout(request):
    """ This view renders the checkout """

    return render(request, 'checkout/checkout.html')
