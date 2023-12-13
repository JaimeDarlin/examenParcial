from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('',views.tiendas,name='tiendas'),
    path('productos',views.productos,name='productos'),
]