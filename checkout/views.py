from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm


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
            order_form.save()
            messages.success(request, 'Profile updated successfully')
            order_form = OrderForm()
            
    template = 'checkout/payment.html'

    return render(request, template)
