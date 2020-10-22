from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',)

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number',
              'country',  'town_or_city', 'app', 'mac', 'mac_pass', 'notes',)

    list_display = ('date', 'full_name',
                    'email', 'country', 'app', 'mac', 'notes',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
