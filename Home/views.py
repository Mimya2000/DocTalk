from django.shortcuts import render


def home(request):
    return render(request, 'Home/index.html')


def about(request):
    return render(request, 'Home/index.html')


def products(request):
    return render(request, 'Home/index.html')


def faqs(request):
    return render(request, 'Home/index.html')


def contact(request):
    return render(request, 'Home/index.html')