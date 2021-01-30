from django.shortcuts import render, redirect, reverse

from django.contrib import messages

from .forms import OrderForm


# Create your views here.

def checkout(request):
    """ This view renders the checkout page """
    bag = request.session.get('bag', {})

    # defensive logic
    if not bag:
        messages.error(request, "Your bag is currently empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
