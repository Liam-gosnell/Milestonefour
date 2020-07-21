from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_BUSINESS_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_BUSINESS_PERCENTAGE / 100)
        free_business_delta = settings.FREE_BUSINESS_THRESHOLD - total
    else:
        delivery = 0
        free_business_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_business_delta': free_business_delta,
        'free_business_threshold': settings.FREE_BUSINESS_THRESHOLD,
        'grand_total': grand_total,
    }

    return context