from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

from profiles.models import UserProfile
from products.models import Product
from .forms import OrderForm
from .models import Order

stripe.api_key = settings.STRIPE_SECRET


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


@login_required()
def checkout_subscription(request):
    profile = UserProfile.objects.get(user=request.user)
    email = profile.user.email
    customer_id = profile.default_stripe_id
    products = Product.objects.all()

    this_customer = stripe.Customer.list(email=email)
    this_data = this_customer.data
    for subscription in this_data:
        have_subscription = subscription.subscriptions.data
        e = len(have_subscription)

    for invoice in this_data:
        have_invoice = invoice.invoice_settings.default_payment_method

    if have_invoice == None:
        message = 'Nu puteti inca activa un abonament. In "Contul meu" accesati butonul "Administrare Abonament", mergeti la "Metoda de plata" si setati metoda de plata ca IMPLICITA. Dupa acest pas puteti activa un abonament nou.'
        return redirect(reverse('profile'))

    if e != 0:
        message = 'Aveti deja un abonament activ. Il puteti administra din "Contul meu"'
        return redirect(reverse('profile'))
    else:
        if request.method == 'POST':
            price_id = request.POST['product_id']

            stripe.Subscription.create(
                customer=customer_id,
                items=[
                    {"price": price_id},
                ],
            )
            return redirect(reverse('profile'))

        template = 'checkout/subscription.html'
        context = {
            'products': products,
        }

        return render(request, template, context)
