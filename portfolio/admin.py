from django.contrib import admin
from .models import Portfolio

# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'description',
        'big_image',
        'approach',
    )

    ordering = ('name',)

admin.site.register(Portfolio, PortfolioAdmin)

