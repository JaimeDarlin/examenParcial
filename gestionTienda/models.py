from django.db import models

# Create your models here.
class tiendasSistema(models.Model):
    direccion = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=40, blank=True, null=True)
    region = models.CharField(max_length=40, blank=True, null=True)
    fechaCreacion = models.DateField(max_length=40, blank=True, null=True)
    telefonoContacto = models.CharField(max_length=15, blank=True, null=True)

class productosSistema(models.Model):
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    precio = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.CharField(max_length=20, blank=True, null=True)
    tiendaProducto = models.ForeignKey(tiendasSistema, on_delete=models.SET_NULL, blank=True, null=True)