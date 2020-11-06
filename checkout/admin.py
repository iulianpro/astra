from django.contrib import admin
from .models import Order
from .models import ActiveSubscription
from django.utils.html import format_html


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',)

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number',
              'country', 'town_or_city', 'app', 'mac', 'mac_pass', 'notes', 'status',)

    list_display = ('date', 'full_name',
                    'email', 'country', 'town_or_city', 'app', 'mac', 'notes', 'status',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)


class ActiveSubscriptionAdmin(admin.ModelAdmin):

    readonly_fields = ('date',)

    list_display = ('sub_customer', 'sub_email', 'sub_date_created', 'sub_period',
                    'sub_date_start', 'sub_date_end', 'sub_price', 'sub_currency', 'status')

    ordering = ('-date',)

    def status(self, ActiveSubscription):
        if ActiveSubscription.sub_status == 'ACTIVATA':
            color = 'green'
            return format_html('<span style="color: {}; font-weight: 800;">{}</span>',
                               color,
                               ActiveSubscription.sub_status,
                               )
        else:
            color = 'red'
            return format_html('<span style="color: {}; font-weight: 800;">{}</span>',
                               color,
                               ActiveSubscription.sub_status,
                               )


admin.site.register(ActiveSubscription, ActiveSubscriptionAdmin)
