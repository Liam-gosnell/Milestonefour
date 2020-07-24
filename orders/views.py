from django.shortcuts import render, get_object_or_404
from .models import Item, ItemTag

from .forms import ItemForm

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


def add_service(request):
    """ Add a product to the store """
    form = ItemForm()
    template = 'orders/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

