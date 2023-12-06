from django.urls import path

from blog_app.apps import BlogAppConfig
from blog_app.views import Blog_appCreateView

# app_name = BlogAppConfig
app_name = 'blog_app'


urlpatterns = [
    path('create/', Blog_appCreateView.as_view(), name='create'),
    # path('', ..., name='list'),
    # path('view/<int:pk/>', ..., name='view'),
    # path('view/<int:pk/>', ..., name='view'),
    # path('delete/<int:pk/', ..., name='delete'),

]
