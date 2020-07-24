from django.db import models
from django.shortcuts import reverse


class ItemTag(models.Model):
    """
    A model for the item tags with selectable
    Bootstrap colours.
    """
    TAG_COLOURS = (
        ('danger', 'Red'),
        ('success', 'Green'),
        ('info', 'Blue'),
        ('warning', 'Yellow'),
        ('secondary', 'Gray')
    )

    name = models.CharField(max_length=10)
    colour = models.CharField(
        choices=TAG_COLOURS, max_length=10, default='Red')

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    A model for the items/products.
    Urls are slug based.
    """
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    description = models.TextField(max_length=70)
    big_description = models.TextField(max_length=400, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    clicks = models.IntegerField(default=0)
    tag = models.ForeignKey(
        ItemTag, null=True, blank=True, on_delete=models.SET_NULL)

    def get_add_to_cart_url(self):
        return reverse('orders:add_to_cart', kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('orders:remove_from_cart', kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.name


