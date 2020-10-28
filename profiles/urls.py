from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('billing/', views.manage_billing, name='billing'),
    path('billing/payment-method/', views.manage_payment_method, name='payment-method'),
    path('billing/billing-address/', views.manage_billing_address, name='billing-address'),
]
