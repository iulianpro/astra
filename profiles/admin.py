from django.contrib import admin
from .models import UserProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'default_country',
        'default_town_or_city',
        'default_app',
        'default_mac',
        'default_notes',
        'default_mac_pass',
    )

    ordering = ('user',)


admin.site.register(UserProfile, ProfileAdmin)