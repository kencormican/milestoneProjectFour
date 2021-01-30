from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Required to send email
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings

# from .models import Contact
from .forms import ContactForm


# Create your views here.

def contact_success(request):
    """ This view returns additional confirmation of the
    message being successful """

    template = 'contact/contact_success.html'

    return render(request, template)


def contact(request):
    """ This view returns the contact page and sends two emails
    if method is post. One to the user and the other to the site admin"""

    store_email = settings.CONTACT_STORE_EMAIL
    store_address = settings.CONTACT_STORE_ADDRESS
    store_phone = settings.CONTACT_STORE_PHONE
    store_location = settings.SITE_MAP_LOCATION

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cust_name = form.cleaned_data['full_name']
            cust_subject = form.cleaned_data['subject']
            cust_email = form.cleaned_data['email']
            cust_message = form.cleaned_data['message']
            subject = 'Customer Query Notification'
            site_email = settings.DEFAULT_FROM_EMAIL
            internal_message = render_to_string(
                'contact/contact_emails/contact_email.txt',
                {'cust_name': cust_name,
                 'cust_email': cust_email,
                 'cust_subject': cust_subject,
                 'cust_message': cust_message}
            )
            outgoing_message = render_to_string(
                'contact/contact_emails/contact_confirmation_email.txt'
            )
            try:
                send_mail(subject, internal_message, cust_email, [site_email])
                send_mail(
                    cust_subject, outgoing_message, site_email, [cust_email])
                messages.success(
                    request, "You've Successfully sent a message to Off Piste"
                )
            except BadHeaderError:
                messages.error(
                    request, "Error Sending Message! Please try again later"
                )
                return HttpResponse('Invalid header found.')

            return redirect('contact_success')

    form = ContactForm
    template = 'contact/contact.html'

    context = {
        'form': form,
        'store_email': store_email,
        'store_address': store_address,
        'store_phone': store_phone,
        'store_location': store_location,
    }
    messages.info(request, """Please use the below
    submission form to raise a query with the team""")

    return render(request, template, context)
