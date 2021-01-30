from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from django.conf import settings
from bag.context_processors import bag_contents

from .forms import OrderForm

import stripe


# Create your views here.

def checkout(request):
    """ This view renders the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})

    # defensive logic
    if not bag:
        messages.error(request, "Your bag is currently empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret_key': stripe_secret_key,
    }

    return render(request, template, context)
