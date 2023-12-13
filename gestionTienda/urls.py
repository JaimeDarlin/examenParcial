from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('',views.tiendas,name='tiendas'),
    path('productos',views.productos,name='productos'),
    path('eliminarTienda/<str:idTienda>',views.eliminarTienda,name='eliminarTienda'),
    path('eliminarProducto/<str:idProducto>',views.eliminarProducto,name='eliminarProducto'),
    path('asignarTienda',views.asignarTienda,name='asignarTienda'),
    path('consultaTienda/<str:idTienda>',views.consultaTienda,name='consultaTienda'),
]