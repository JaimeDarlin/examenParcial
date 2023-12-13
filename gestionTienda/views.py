from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import tiendasSistema, productosSistema

# Create your views here.
def index(request):
    return render(request,'tiendas.html')

def tiendas(request):
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        provincia = request.POST.get('provincia')
        region = request.POST.get('region')
        fechaCreacion = request.POST.get('fechaCreacion')
        telefonoContacto = request.POST.get('telefonoContacto')
        tiendasSistema.objects.create(
            direccion=direccion,
            provincia=provincia,
            region=region,
            fechaCreacion=fechaCreacion,
            telefonoContacto=telefonoContacto
        )
        return HttpResponseRedirect(reverse('gestionTiendaMod:tiendas'))
    return render(request,'tiendas.html',{
        'listaTiendas':tiendasSistema.objects.all().order_by('id')
    })

def productos(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        productosSistema.objects.create(
            descripcion=descripcion,
            codigo=codigo,
            precio=precio,
            cantidad=cantidad,
        )
        return HttpResponseRedirect(reverse('gestionTiendaMod:productos'))
    return render(request,'productos.html',{
        'productosTotales':productosSistema.objects.all().order_by('id'),
        'tiendasTotales':tiendasSistema.objects.all().order_by('id')
    })