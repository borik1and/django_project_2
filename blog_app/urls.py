from django.urls import path

from blog_app.apps import BlogAppConfig
from blog_app.views import (Blog_appCreateView, Blog_appListView, Blog_appDetailView,
                            Blog_appUpdateView, Blog_appDeleteView)

# app_name = BlogAppConfig
app_name = 'blog_app'


urlpatterns = [
    path('create/', Blog_appCreateView.as_view(), name='create'),
    path('list', Blog_appListView.as_view(), name='list'),
    path('view/<int:pk>/', Blog_appDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', Blog_appUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', Blog_appDeleteView.as_view(), name='delete'),

]
