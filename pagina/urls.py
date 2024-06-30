from django.urls import path
from .views import menu, home, productoList, productoAdd, productoEdit, productoDel

urlpatterns = [
    path('menu',menu, name='menu'),
    path('home',home, name='home'),
    path('productoList/', productoList, name='productoList'),
    path('productoAdd/', productoAdd, name='productoAdd'),
    path('productoEdit/<str:pk>', productoEdit, name='productoEdit'),
    path('productoDel/<str:pk>', productoDel, name='productoDel'),
]
