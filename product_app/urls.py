
from django.urls import path

from product_app import views
from product_app.apps import PtoductAppConfig

app_name = PtoductAppConfig.name


urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('about', views.about),
    path('catalog', views.catalog),

]