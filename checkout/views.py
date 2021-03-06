from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.html import format_html
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import stripe
import random
import string
import time

from django.contrib.auth.models import User
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from products.models import Product
from .forms import OrderForm
from .models import Order
from .models import ActiveSubscription

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
            return redirect(reverse('subscription'))

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

        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            profile_data = {
                'default_phone_number': request.POST['phone_number'],
                'default_country': request.POST['country'],
                'default_town_or_city': request.POST['town_or_city'],
                'default_app': request.POST['app'],
                'default_mac': request.POST['mac'],
                'default_mac_pass': request.POST['mac_pass'],
            }

            user_data = request.POST['full_name']

            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

            fname_lname = user_data.split()
            lname = fname_lname[-1]
            fname = ' '.join(map(str, fname_lname[:-1]))

            user = request.user

            user.first_name = fname
            user.last_name = lname
            user.save()

        if request.user.is_authenticated == False:
            def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))

            this_username = request.POST['email']
            this_password = random_string_generator()
            this_email = request.POST['email']

            if not User.objects.filter(username=this_username).exists():
                user = User.objects.create_user(
                    username=this_username,
                    password=this_password,
                    email=this_email,
                )
                user.save()
                user = authenticate(username=this_username,
                                    password=this_password)
                if user is not None:
                    login(request, user)

                    subject = 'Contul tau Astra.IPTV a fost creat cu succes'
                    body_email = 'Datele tale de logare sunt: Username: ' + \
                        this_username + '; Password: ' + this_password
                    sender = settings.DEFAULT_FROM_EMAIL
                    receiver = this_username
                    send_mail(subject, body_email, sender, [
                              receiver, ], fail_silently=False,)

                    user_data = request.POST['full_name']
                    fname_lname = user_data.split()
                    lname = fname_lname[-1]
                    fname = ' '.join(map(str, fname_lname[:-1]))
                    user = request.user
                    user.first_name = fname
                    user.last_name = lname
                    user.save()

                    profile = UserProfile.objects.get(user=request.user)
                    profile.default_phone_number = request.POST['phone_number']
                    profile.default_country = request.POST['country']
                    profile.default_town_or_city = request.POST['town_or_city']
                    profile.default_app = request.POST['app']
                    profile.default_mac = request.POST['mac']
                    profile.default_mac_pass = request.POST['mac_pass']
                    profile.save()

                    # Keep in mind: to send the login details to the User
            else:
                messages.error(
                    request, 'Aveti deja un cont cu aceste date, pentru a continua va rugam sa va autentificati')
                return redirect(reverse('account_login'))

        template = 'checkout/payment.html'
        return render(request, template)
    else:
        messages.error(
            request, 'Nu sunteti autorizat sa accesati aceasta pagina!')
        return redirect(reverse('home'))


def checkout_success(request, *callback_args, **callback_kwargs):
    if not request.session.get('order_form_submitted', False):
        messages.error(
            request, 'Nu sunteti autorizat sa accesati aceasta pagina!')
        return redirect(reverse('home'))
    else:
        order_paid = Order.objects.last()
        order_paid.status = 'PLATITA'
        order_paid.save()

        if request.user.is_authenticated:
            profile = get_object_or_404(UserProfile, user=request.user)
            email = profile.user.email
            stripe_id = profile.default_stripe_id

            if stripe_id == None:
                this_customer = stripe.Customer.list(email=email)
                this_data = this_customer.data
                for data in this_data:
                    customer_id = data.id
                    profile.default_stripe_id = customer_id
                    profile.save()

        request.session['order_form_submitted'] = False

        template = 'checkout/checkout_success.html'
        return render(request, template)


def checkout_canceled(request, *callback_args, **callback_kwargs):
    if not request.session.get('order_form_submitted', False):
        messages.error(
            request, 'Nu sunteti autorizat sa accesati aceasta pagina!')
        return redirect(reverse('home'))
    else:
        order_canceled = Order.objects.last()
        order_canceled.status = 'ANULATA'
        order_canceled.save()
        request.session['order_form_submitted'] = False

        template = 'checkout/checkout_canceled.html'
        return render(request, template)


@login_required()
def checkout_subscription(request):
    profile = UserProfile.objects.get(user=request.user)
    email = profile.user.email
    customer_id = profile.default_stripe_id
    products = Product.objects.all()

    if customer_id != None:
        if (profile.default_country == None and profile.default_town_or_city == None and profile.default_app and profile.default_mac == None):
            messages.info(
                request, 'Pentru a activa un abonament este necesar sa aveti datele de profil marcate cu (*) actualizate')
            return redirect(reverse('profile'))
    else:
        messages.warning(
            request, 'Puteti activa un abonament numai dupa ce comandati un Test 24H')
        return redirect(reverse('profile'))

    this_customer = stripe.Customer.list(email=email)
    this_data = this_customer.data

    have_default_payment_method = this_data[0].invoice_settings.default_payment_method

    if have_default_payment_method == None:
        # interogate API to retrieve payment_method
        customer_payment_method_list = stripe.PaymentMethod.list(
            customer=customer_id,
            type="card",
        )

        customer_default_payment_method = customer_payment_method_list.data[0].id
        # interogate API to set up default payment_method
        stripe.Customer.modify(
            customer_id,
            invoice_settings={
                "default_payment_method": customer_default_payment_method
            },
        )

    for subscription in this_data:
        have_subscription = subscription.subscriptions.data
        e = len(have_subscription)

    if e != 0:
        messages.info(
            request, 'Aveti deja un abonament activ. Il puteti administra din aceasta pagina')
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
            this_customer = stripe.Customer.list(email=email)
            this_data = this_customer.data

            format = "%d/%m/%Y"
            date_created = this_data[0].subscriptions.data[0].created
            str_date_created = time.strftime(
                format, time.localtime(date_created))

            date_start = this_data[0].subscriptions.data[0].current_period_start
            str_date_start = time.strftime(format, time.localtime(date_start))

            date_end = this_data[0].subscriptions.data[0].current_period_end
            str_date_end = time.strftime(format, time.localtime(date_end))

            import_status = this_data[0].subscriptions.data[0].plan.active
            if import_status == True:
                this_status = 'ACTIVATA'
            else:
                this_status = 'DEZACTIVATA'

            interval = this_data[0].subscriptions.data[0].plan.interval
            interval_count = this_data[0].subscriptions.data[0].plan.interval_count

            if interval == 'month':
                set_interval = interval_count
            else:
                set_interval = 12

            try:
                active_subscription = ActiveSubscription.objects.get(
                    sub_customer=request.user)
                active_subscription.sub_date_created = str_date_created,
                active_subscription.sub_period = set_interval,
                active_subscription.sub_date_start = str_date_start,
                active_subscription.sub_date_end = str_date_end,
                active_subscription.sub_price = this_data[0].subscriptions.data[0].plan.amount/100,
                active_subscription.sub_currency = this_data[0].subscriptions.data[0].plan.currency.upper(
                ),
                active_subscription.sub_status = this_status
                active_subscription.save()

            except ActiveSubscription.DoesNotExist:
                active_subscription = ActiveSubscription(
                    sub_customer=request.user,
                    sub_email=request.user.first_name + ' ' + request.user.last_name,
                    sub_date_created=str_date_created,
                    sub_period=set_interval,
                    sub_date_start=str_date_start,
                    sub_date_end=str_date_end,
                    sub_price=this_data[0].subscriptions.data[0].plan.amount/100,
                    sub_currency=this_data[0].subscriptions.data[0].plan.currency.upper(
                    ),
                    sub_status=this_status
                )
                active_subscription.save(force_insert=True)

                this_price = this_data[0].subscriptions.data[0].plan.amount/100
                subject = 'Abonament nou activat pentru: ' + request.user.email
                body_email = 'Userul ' + request.user.email + \
                    ' a activat un nou abonament de €' + str(int(this_price)) + \
                    ' cu statusul ' + this_status + '.'
                sender = settings.DEFAULT_FROM_EMAIL
                receiver = settings.DEFAULT_FROM_EMAIL
                send_mail(subject, body_email, sender, [
                    receiver, ], fail_silently=False,)

            messages.success(
                request, 'Abonamentul dvs, a fost activat cu succes!')
            return redirect(reverse('profile'))

        template = 'checkout/subscription.html'
        context = {
            'products': products,
        }

        return render(request, template, context)
