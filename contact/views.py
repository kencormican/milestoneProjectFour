from django.shortcuts import render

# from .models import Contact
from .forms import ContactForm


# Create your views here.

def contact(request):
    """ This view returns the contact page """

    form = ContactForm
    template = 'contact/contact.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
