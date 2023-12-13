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

def consultaTienda(request,idTienda):
    objTienda = tiendasSistema.objects.get(id=idTienda)
    productosRelacionados = objTienda.productossistema_set.all()
    listaProductos = []
    for productoInfo in productosRelacionados:
        listaProductos.append([
            productoInfo.descripcion,
            productoInfo.codigo,
            productoInfo.precio,
            productoInfo.cantidad
        ])
    print(productosRelacionados)
    return JsonResponse({
        'listaProductos':listaProductos,
        'direccion':objTienda.direccion,
        'fechaCreacion':objTienda.fechaCreacion,
        'telefonoContacto':objTienda.telefonoContacto,
    })

def eliminarTienda(request, idTienda):
    objTienda = tiendasSistema.objects.get(id=idTienda)
    objTienda.delete()
    return HttpResponseRedirect(reverse('gestionTiendaMod:tiendas'))

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

def asignarTienda(request):
    if request.method == 'POST':
        idProducto = request.POST.get('productoSeleccionado')
        idTienda = request.POST.get('tiendaSeleccionada')
        objProducto = productosSistema.objects.get(id=idProducto)
        objTienda = tiendasSistema.objects.get(id=idTienda)
        #objProducto = productosSistema.objects.get(productoAsociado=objProducto)
        objProducto.tiendaProducto = objTienda
        objProducto.save()
        return HttpResponseRedirect(reverse('gestionTiendaMod:productos'))
    

def eliminarProducto(request, idProducto):
    objProducto = productosSistema.objects.get(id=idProducto)
    objProducto.delete()
    return HttpResponseRedirect(reverse('gestionTiendaMod:productos'))