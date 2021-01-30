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

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            You must set it in your environment?')

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request):
    """ This view will render a confirmation of successful
    checkout operation the about page """

    template = 'checkout/checkout_success.html'

    context = {
    }

    return render(request, template, context)
