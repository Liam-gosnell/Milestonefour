from django.db import models

# Create your models here.

class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolios'

        
    name = models.CharField(max_length=254)
    title = models.CharField(max_length=254, null=True, blank=True)
    slug = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    portfolio_image = models.ImageField(null=True, blank=True)
    specific_design_drop = models.ImageField(null=True, blank=True)
    big_image = models.ImageField(null=True, blank=True)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    bullet_1 = models.TextField()
    bullet_2 = models.TextField()
    bullet_3 = models.TextField()
    bullet_4 = models.TextField()
    approach = models.TextField()

    def __str__(self):
        return self.name


