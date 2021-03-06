from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_payment_id',
                       'user_profile',)

    fields = ('order_number', 'full_name', 'email', 'date', 'phone_number',
              'street_address', 'house_number', 'addition', 'postcode', 'city',
              'country', 'delivery_cost', 'order_total', 'grand_total',
              'original_bag', 'stripe_payment_id')

    list_display = ('order_number', 'date', 'full_name', 'city',
                    'delivery_cost', 'order_total', 'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
