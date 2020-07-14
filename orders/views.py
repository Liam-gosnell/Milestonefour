from django.shortcuts import render
from .models import Item

# Create your views here.

def all_services(request):
    """ A view to show all services """

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'orders/services.html', context)