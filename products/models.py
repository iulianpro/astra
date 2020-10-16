from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description_1 = models.CharField(max_length=254, null=True, blank=True)
    description_2 = models.CharField(max_length=254, null=True, blank=True)
    description_3 = models.CharField(max_length=254, null=True, blank=True)
    description_4 = models.CharField(max_length=254, null=True, blank=True)
    description_5 = models.CharField(max_length=254, null=True, blank=True)
    description_6 = models.CharField(max_length=254, null=True, blank=True)
    description_7 = models.CharField(max_length=254, null=True, blank=True)
    description_8 = models.CharField(max_length=254, null=True, blank=True)
    description_9 = models.CharField(max_length=254, null=True, blank=True)
    description_10 = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.category.friendly_name)
