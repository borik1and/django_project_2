from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog_app.models import Blog_app
from pytils.translit import slugify

class Blog_appCreateView(CreateView):
    model = Blog_app
    fields = ('title', 'body', 'creation_date', 'publication', 'preview')
    # template_name = 'blog_app/blog_app_form.html'
    success_url = reverse_lazy('blog_app:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class Blog_appListView(ListView):
    model = Blog_app

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class Blog_appDetailView(DetailView):
    model = Blog_app

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_num += 1
        obj.save()
        return obj


class Blog_appUpdateView(UpdateView):
    model = Blog_app
    fields = ('title', 'body', 'creation_date', 'publication')
    template_name = 'blog_app/blog_app_form.html'
    # success_url = reverse_lazy('blog_app:list')
    queryset = Blog_app.objects.all()

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_app:view', args=[self.kwargs.get('pk')])


class Blog_appDeleteView(DeleteView):
    model = Blog_app
    success_url = reverse_lazy('blog_app:list')
