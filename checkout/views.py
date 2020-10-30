from django.shortcuts import render
from django.contrib import messages

from profiles.models import UserProfile
from .forms import OrderForm
from .models import Order


def checkout(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        customer_id = profile.default_stripe_id

        if customer_id == None:
            try:
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'town_or_city': profile.default_town_or_city,
                    'app': profile.default_app,
                    'mac': profile.default_mac,
                    'mac_pass': profile.default_mac_pass,
                    'notes': profile.default_notes,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            template = 'home/index.html'
            return render(request, template)

    else:
        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


def checkout_payment(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            request.session['order_form_submitted'] = True
            order_form.save()
            order_form = OrderForm()

        template = 'checkout/payment.html'
        return render(request, template)
    else:
        template = 'home/index.html'
        return render(request, template)


def checkout_success(request, *callback_args, **callback_kwargs):
    if not request.session.get('order_form_submitted', False):

        template = 'home/index.html'
        return render(request, template)
    else:
        # order_paid = Order.objects.last()
        # order_paid.status = 'PLATITA'
        # order_paid.save()
        request.session['order_form_submitted'] = False

        template = 'checkout/checkout_success.html'
        return render(request, template)


def checkout_canceled(request, *callback_args, **callback_kwargs):
    if not request.session.get('order_form_submitted', False):

        template = 'home/index.html'
        return render(request, template)
    else:
        # order_canceled = Order.objects.last()
        # order_canceled.status = 'ANULATA'
        # order_canceled.save()
        request.session['order_form_submitted'] = False

        template = 'checkout/checkout_canceled.html'
        return render(request, template)
