from django.urls import path
from .views import index, alemania, brasil, argentina, colocolo, cololocal, comprar, madrid, manchester, psg, restodelmundo, selechile, uchile, udechilelocal, productoList, productoAdd, productoEdit, productoDel


urlpatterns = [
    path('', index, name='index'),
    path('alemania/', alemania, name='alemania'),
    path('brasil/', brasil, name='brasil'),
    path('argentina/', argentina, name='argentina'),
    path('colocolo/', colocolo, name='colocolo'),
    path('cololocal/', cololocal, name='cololocal'),
    path('comprar/', comprar, name='comprar'),
    path('madrid/', madrid, name='madrid'),
    path('manchester/', manchester, name='manchester'),
    path('psg/', psg, name='psg'),
    path('restodelmundo/', restodelmundo, name='restodelmundo'),
    path('selechile/', selechile, name='selechile'),
    path('uchile/', uchile, name='uchile'),
    path('udechilelocal/', udechilelocal, name='udechilelocal'),
    path('productoList/', productoList, name='productoList'),
    path('productoAdd/', productoAdd, name='productoAdd'),
    path('productoEdit/<str:pk>', productoEdit, name='productoEdit'),
    path('productoDel/<str:pk>', productoDel, name='productoDel'),
]
