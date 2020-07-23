from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GzKHFKu9KZOmvLwiwdnEg5TCSnjob6Sdt6302SOmH4TLhSCZN8qUhq5GraS9s3rvnsgOGBFc3WBp2YiVflK4nV300NWExYjlO',
        'client_secret': 'test client_secret', 
    }

    return render(request, template, context)