from django.urls import path, include
from product_app.views import CatalogListView, IndexListView, AboutView, Product_appCreateView, Product_appUpdateView, \
    ProductDetailView, categories
from django.views.decorators.cache import cache_page

app_name = 'product_app'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('create/', Product_appCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', Product_appUpdateView.as_view(), name='update_product'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('categories/', categories, name='categories'),
]
