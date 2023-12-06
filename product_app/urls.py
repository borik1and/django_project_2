from django.urls import path
from product_app.views import CatalogListView, IndexListView, AboutView
from product_app import views
# from product_app.apps import ProductAppConfig

# app_name = ProductAppConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('index', IndexListView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('catalog', CatalogListView.as_view(), name='catalog'),
]
