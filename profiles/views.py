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
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    email = profile.user.email
    fname = profile.user.first_name
    lname = profile.user.last_name

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'email': email,
        'fname': fname,
        'lname': lname,
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
