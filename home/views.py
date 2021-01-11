from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def about_us(request):
    return render(request, 'home/about-us.html')


def contact(request):
    return render(request, 'home/contact.html')


def faq(request):
    return render(request, 'home/faq.html')


def terms(request):
    return render(request, 'home/terms.html')


def conditions(request):
    return render(request, 'home/conditions.html')
