from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def all_services(request):
    """ A view to show all services """

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'orders/services.html', context)


def service_detail(request, item_id):
    """ A view to show individual service details """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'orders/service_detail.html', context)

