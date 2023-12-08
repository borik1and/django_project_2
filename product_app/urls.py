from django.urls import path
from product_app.views import CatalogListView, IndexListView, AboutView

app_name = 'product_app'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('index', IndexListView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('catalog', CatalogListView.as_view(), name='catalog'),
]
