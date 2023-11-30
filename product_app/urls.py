
from django.urls import path

from product_app import views


urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('about', views.about),

]