from django.shortcuts import render
from profiles.models import UserProfile
from .models import Product

# Create your views here.


def all_products(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        customer_id = profile.default_stripe_id

        products = Product.objects.all()
        context = {
            'products': products,
            'customer_id': customer_id,
        }
        return render(request, 'products/products.html', context)
    else:
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'products/products.html', context)
