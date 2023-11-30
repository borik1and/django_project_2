from django.shortcuts import render


def index(request):
    return render(request, 'product_app/index.html')


def about(request):
    return render(request, 'product_app/about.html')
