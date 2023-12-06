from django.shortcuts import render
from django.views.generic import CreateView
from blog_app.models import Blog_app


class Blog_appCreateView(CreateView):
    model = Blog_app
    fields = ('title', 'body', 'creation_date', 'publication')
    template_name = 'blog_app/blog_form.html'
