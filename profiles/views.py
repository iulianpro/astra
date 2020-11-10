from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import stripe
import time

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import ActiveSubscription

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
            messages.success(
                request, 'Informatiile au fost salvate cu succes')

    form = UserProfileForm(instance=profile)
    email = profile.user.email
    fname = profile.user.first_name
    lname = profile.user.last_name

    this_customer = stripe.Customer.list(email=email)
    this_data = this_customer.data

    if profile.default_stripe_id == None:
        for data in this_data:
            stripe_id = data.id
            profile.default_stripe_id = stripe_id
            profile.save()

    for sub in this_data:
        have_sub = sub.subscriptions.data
        length = len(have_sub)
        profile.default_subscription = length
        profile.save()

    profile = get_object_or_404(UserProfile, user=request.user)
    customer_id = profile.default_stripe_id
    subscription = profile.default_subscription

    if subscription != 0:
        format = "%d/%m/%Y"
        date_created = this_data[0].subscriptions.data[0].created
        str_date_created = time.strftime(
            format, time.localtime(date_created))
        date_start = this_data[0].subscriptions.data[0].current_period_start
        str_date_start = time.strftime(format, time.localtime(date_start))
        date_end = this_data[0].subscriptions.data[0].current_period_end
        str_date_end = time.strftime(format, time.localtime(date_end))
        import_status = this_data[0].subscriptions.data[0].cancel_at_period_end

        if import_status != True:
            this_status = 'ACTIVATA'
        else:
            this_status = 'DEZACTIVATA'

        interval = this_data[0].subscriptions.data[0].plan.interval
        interval_count = this_data[0].subscriptions.data[0].plan.interval_count

        if interval == 'month':
            set_interval = interval_count
        else:
            set_interval = 12

        active_subscription = ActiveSubscription.objects.get(
            sub_customer=request.user)

        now_sub_price = active_subscription.sub_price
        now_sub_status = active_subscription.sub_status

        a = str_date_created,
        active_subscription.sub_date_created = a[0]
        b = set_interval,
        active_subscription.sub_period = b[0]
        c = str_date_start,
        active_subscription.sub_date_start = c[0]
        d = str_date_end,
        active_subscription.sub_date_end = d[0]
        e = this_data[0].subscriptions.data[0].plan.amount/100,
        active_subscription.sub_price = e[0]
        f = this_data[0].subscriptions.data[0].plan.currency.upper(
        ),
        active_subscription.sub_currency = f[0]
        active_subscription.sub_status = this_status

        if now_sub_price != e[0] or now_sub_status != this_status:
            subject = 'Modificare abonament user ' + request.user.email
            body_email = 'Userul ' + request.user.email + ' a modificat abonamentul de €' + str(now_sub_price) + \
                ' in abonament de €' + \
                str(int(e[0])) + ' si statusul din ' + \
                now_sub_status + ' in ' + this_status + '.'
            sender = settings.DEFAULT_FROM_EMAIL
            receiver = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, body_email, sender, [
                      receiver, ], fail_silently=False,)

        active_subscription.save()

    try:
        if length != 0:
            print(1)

            invoice = have_sub[0].latest_invoice
            customer_invoice = stripe.Invoice.retrieve(
                invoice,
            )
            hosted_invoice_url = customer_invoice.hosted_invoice_url
            import_balance = this_data[0].balance
            balance = -import_balance/100

            template = 'profiles/profile.html'
            context = {
                'form': form,
                'email': email,
                'fname': fname,
                'lname': lname,
                'customer_id': customer_id,
                'subscription': subscription,
                'hosted_invoice_url': hosted_invoice_url,
                'balance': balance,
                'b': active_subscription.sub_period,
                'c': active_subscription.sub_date_start,
                'd': active_subscription.sub_date_end,
                'this_status': this_status,
            }
            return render(request, template, context)
        else:
            print(2)
            print('Customer doesn\'t have invoice')
    except:
        print(3)
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

    print(4)
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
