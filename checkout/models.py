import uuid
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField


class Order(models.Model):
    APP_CHOICE = [
        ('smart_iptv', 'Smart IPTV'),
        ('set_iptv', 'Set IPTV'),
        ('net_iptv', 'Net IPTV'),
        ('iptv_extreme', 'IPTV Extreme'),
        ('mag_device', 'Dispozitiv MAG'),
        ('stb_device', 'Dispozitiv STB'),
        ('another_device', 'Alt dispozitiv'),
    ]
    APP_CHOICE_AND_EMPTY = [('','Selecteza aplicatia *')] + APP_CHOICE
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    app = models.CharField(max_length=40, choices=APP_CHOICE_AND_EMPTY)
    mac = models.CharField(max_length=40, null=False, blank=False)
    mac_pass = models.CharField(max_length=40, null=True, blank=True)
    notes = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=40, null=True, blank=True, default='STAND-BY')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
