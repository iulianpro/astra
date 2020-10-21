from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    APP_CHOICE = [
        ('select', 'Selecteaza aplicatia'),
        ('smart_iptv', 'Smart IPTV'),
        ('set_iptv', 'Set IPTV'),
        ('net_iptv', 'Net IPTV'),
        ('iptv_extreme', 'IPTV Extreme'),
        ('mag_device', 'Dispozitiv MAG'),
        ('stb_device', 'Dispozitiv STB'),
        ('another_device', 'Alt dispozitiv'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_app = models.CharField(max_length=40, choices=APP_CHOICE, default='select')
    default_mac = models.CharField(max_length=40, null=True, blank=True)
    default_mac_pass = models.CharField(max_length=40, null=True, blank=True)
    default_notes = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
