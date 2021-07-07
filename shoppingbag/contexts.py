from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    bag_items = 0
    total = 0
    product_count = 0

    if total <= 0:
        delivery = 0
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD
    elif total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total + Decimal(settings.STANDARD_DELIVERY)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context
