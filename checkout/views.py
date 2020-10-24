from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm
from .models import Order


def checkout(request):
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


def checkout_success(request, *callback_args, **callback_kwargs):
    if not request.session.get('order_form_submitted', False):
        template = 'home/index.html'
        return render(request, template)
    else:
        template = 'checkout/checkout_success.html'
        return render(request, template)


def checkout_canceled(request, *callback_args, **callback_kwargs):
    order_to_cancel = Order.objects.latest('id')
    order_canceled = order_to_cancel.id
    print(type(order_canceled))
    
    if not request.session.get('order_form_submitted', False):
        template = 'home/index.html'
        return render(request, template)
    else:
        template = 'checkout/checkout_canceled.html'

        return render(request, template)
