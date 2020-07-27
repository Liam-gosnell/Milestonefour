from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from orders.models import Item


def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0
    bag = request.session.get('bag', {})
    print(bag)
    for item_id, quantity in bag.items():
        item = get_object_or_404(Item, pk=item_id)
        total += quantity * item.price
        item_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'item': item,
        })

    if total < settings.FREE_BUSINESS_THRESHOLD:
        business = total * Decimal(settings.STANDARD_BUSINESS_PERCENTAGE / 100)
        free_business_delta = settings.FREE_BUSINESS_THRESHOLD - total
    else:
        business = 0
        free_business_delta = 0

    grand_total = business + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
        'business': business,
        'free_business_delta': free_business_delta,
        'free_business_threshold': settings.FREE_BUSINESS_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
