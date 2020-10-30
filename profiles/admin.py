from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
        'default_phone_number',
        'default_country',
        'default_town_or_city',
        'default_app',
        'default_mac',
        'default_notes',
        'default_stripe_id',
        'default_subscription',
    )

    ordering = ('user',)


admin.site.register(UserProfile, ProfileAdmin)
