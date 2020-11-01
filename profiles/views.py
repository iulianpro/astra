from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

from .models import UserProfile
from .forms import UserProfileForm

stripe.api_key = settings.STRIPE_SECRET
return_url = 'http://127.0.0.1:8000/profile/'


@login_required()
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informatiile au fost salvate in contul dvs.')

    form = UserProfileForm(instance=profile)
    email = profile.user.email
    fname = profile.user.first_name
    lname = profile.user.last_name

    this_customer = stripe.Customer.list(email=email)
    this_data = this_customer.data

    for data in this_data:
        customer_id = data.id
        profile.default_stripe_id = customer_id
        profile.save()

    for sub in this_data:
        have_sub = sub.subscriptions.data
        length = len(have_sub)
        profile.default_subscription = length
        profile.save()

    profile = get_object_or_404(UserProfile, user=request.user)
    customer_id = profile.default_stripe_id
    subscription = profile.default_subscription

    try:
        if length != 0:
            invoice = have_sub[0].latest_invoice
            customer_invoice = stripe.Invoice.retrieve(
                invoice,
            )
            hosted_invoice_url = customer_invoice.hosted_invoice_url
            template = 'profiles/profile.html'
            context = {
                'form': form,
                'email': email,
                'fname': fname,
                'lname': lname,
                'customer_id': customer_id,
                'subscription': subscription,
                'hosted_invoice_url': hosted_invoice_url,
            }
            return render(request, template, context)
        else:
            print('Customer doesn\'t have invoice')
    except:
        template = 'profiles/profile.html'
        context = {
            'form': form,
            'email': email,
            'fname': fname,
            'lname': lname,
            'customer_id': customer_id,
            'subscription': subscription,
        }
        return render(request, template, context)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'email': email,
        'fname': fname,
        'lname': lname,
        'customer_id': customer_id,
        'subscription': subscription,
    }
    return render(request, template, context)


@login_required()
def manage_billing(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    customer = profile.default_stripe_id
    portal_session = stripe.billing_portal.Session.create(
        customer=customer,
        return_url=return_url,
    )
    return redirect(portal_session.url)


@login_required()
def manage_payment_method(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    customer = profile.default_stripe_id
    portal_session = stripe.billing_portal.Session.create(
        customer=customer,
        return_url=return_url,
    )
    url = portal_session.url
    payment_method = '/payment-methods'
    url_payment_method = url + payment_method

    return redirect(url_payment_method)


@login_required()
def manage_billing_address(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    customer = profile.default_stripe_id
    portal_session = stripe.billing_portal.Session.create(
        customer=customer,
        return_url=return_url,
    )
    url = portal_session.url
    billing_address = '/customer/update'
    url_payment_method = url + billing_address

    return redirect(url_payment_method)
