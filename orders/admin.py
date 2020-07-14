from django.contrib import admin
from .models import Item, ItemTag 


class ItemTagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'colour'
    )


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'tag',
        'price',
        'clicks'
    )

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemTag, ItemTagAdmin)
