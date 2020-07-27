from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    """ A view to return the Contact page """

    return render(request, 'contact/contact.html')



