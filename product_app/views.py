from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from product_app.models import Product
from django.views import View


class IndexListView(ListView):
    model = Product
    template_name = 'product_app/index_list.html'


class CatalogListView(ListView):
    model = Product
    template_name = 'product_app/catalog_list.html'


class AboutView(View):
    template_name = 'product_app/about.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')

        print(f'имя: {name}, имеил: {email}, сообщение: {message}.')
        with open('message.txt', 'a') as t_f:
            t_f.write(f'имя: {name}, имеил: {email}, сообщение: {message}.')
        return render(request, 'product_app/about.html')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
