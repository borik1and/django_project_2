from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from product_app.forms import ProductForm, VersionForm
from product_app.models import Product, Version, Category
from django.views import View


class IndexListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_app/index_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        # Фильтруем продукты по владельцу (owner) текущего пользователя
        return super().get_queryset().filter(
            owner=self.request.user
        )


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class CatalogListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_app/catalog_list.html'

    def get_queryset(self):
        # Фильтруем продукты по владельцу (owner) текущего пользователя
        return super().get_queryset().filter(
            owner=self.request.user
        )


class AboutView(LoginRequiredMixin, View):
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


class Product_appCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_app/product_form.html'
    success_url = reverse_lazy('product_app:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class Product_appUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_app/product_form.html'
    success_url = reverse_lazy('product_app:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
            # информацию об активной версии в контекст
            context_data['active_version'] = self.object.versions.filter(version_flag=True).first()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)
