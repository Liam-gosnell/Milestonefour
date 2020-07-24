from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
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
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('add_service'))
        else:
            messages.error(request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ItemForm()

    template = 'orders/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_service(request, item_id):
    """ Edit a service in the store """
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[item.id]))
        else:
            messages.error(request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'orders/edit_service.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)