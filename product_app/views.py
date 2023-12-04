from django.shortcuts import render

from product_app.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Главная'
    }
    return render(request, 'product_app/index.html', context)


def catalog(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Главная'
    }
    return render(request, 'product_app/catalog.html', context)


def about(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(f'имя: {name}, имеил: {email}, сообщение: {message}.')
        with open('message.txt', 'a') as t_f:
            t_f.write(f'имя: {name}, имеил: {email}, сообщение: {message}.')
    return render(request, 'product_app/about.html')
