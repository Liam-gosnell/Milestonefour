from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number',
                       'order_total',
                       'grand_total',)

    fields = ('order_number', 'full_name',
              'email', 'phone_number', 'country',
              'order_total', 
              'grand_total',)

    list_display = ('order_number', 'full_name',
                    'order_total',
                    'grand_total',)


admin.site.register(Order, OrderAdmin)