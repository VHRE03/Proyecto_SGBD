from enum import unique
from pyexpat import model
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name = 'Nombre')

    def __str__(self):
        fila = "ID: " + str(self.id_autor) + " - " + "Nombre: " + self.nombre
        return fila 

class editoriales(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name = 'Nombre')

    def __str__(self):
        fila = "ID: " + str(self.id_editorial) + " - " + "Nombre: " + self.nombre
        return fila 

class libros(models.Model):
    id_libro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 100, blank = True, null = True,verbose_name = 'Titulo')
    edicion = models.IntegerField(verbose_name = 'Edicion')
    anio = models.IntegerField(verbose_name = 'Año')
    paginas = models.IntegerField(verbose_name = 'Numero de paginas')
    volumen = models.IntegerField(verbose_name = 'Volumen')
    autor = models.ForeignKey(autores, on_delete=models.PROTECT, verbose_name = 'Autor')
    editorial = models.ForeignKey(editoriales, on_delete=models.PROTECT, verbose_name = 'Editorial')

    def __str__(self):
        fila = "ID: " + str(self.id_libro) + " - " + "Nombre: " + self.nombre
        return fila

class lectores(models.Model):
    no_tarjeta = models.IntegerField(primary_key = True, unique = True, null=False, verbose_name = 'Número de tarjeta')
    nombre = models.CharField(max_length = 100, verbose_name = 'Nombre')
    direccion = models.CharField(max_length = 200, verbose_name = 'Dirección')
    telefono = models.IntegerField(verbose_name = 'Teléfono')
    correo = models.EmailField(verbose_name = 'Correo electronico')

class sucursales(models.Model):
    id_sucursal = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 100, verbose_name = 'Nombre')
    direccion = models.CharField(max_length = 200, verbose_name = 'Dirección')

class prestamos(models.Model):
    id_prestamo = models.AutoField(primary_key = True)
    id_sucursal = models.ForeignKey(sucursales, on_delete=models.PROTECT, verbose_name = 'Sucursal')
    no_tarjeta = models.ForeignKey(lectores, on_delete=models.PROTECT, verbose_name = 'Lector')
    fecha_inicio = models.DateField(verbose_name = 'Fecha de inicio de prestamo')
    fecha_fin = models.DateField(verbose_name = 'Fecha de finalización de prestamo')
    estado = models.CharField(max_length = 100, null=True, verbose_name = 'Estado')
    
class libro_prestamo(models.Model):
    prestamo = models.ForeignKey(prestamos, on_delete=models.CASCADE, verbose_name = 'id_prestamo')
    libro = models.ForeignKey(libros, on_delete=models.PROTECT, verbose_name = 'Libro')
    
class copias_libros(models.Model):
    id = models.AutoField(primary_key = True)
    id_libro = models.ForeignKey(libros, on_delete=models.PROTECT, verbose_name = 'Libro')
    id_sucursal = models.ForeignKey(sucursales, on_delete=models.PROTECT, verbose_name = 'Sucursal')
    no_copias = models.IntegerField(verbose_name = 'Número de copias')

class empleados(models.Model):
    id_empleado = models.IntegerField(primary_key = True, unique = True)
    id_sucursal = models.ForeignKey(sucursales, on_delete=models.PROTECT, verbose_name = 'Sucursal')
    nombre = models.CharField(max_length = 100, verbose_name = 'Nombre')
    direccion = models.CharField(max_length = 200, verbose_name = 'Dirección')
    telefono = models.IntegerField(verbose_name = 'Teléfono')
    correo = models.EmailField(verbose_name = 'Correo electronico')
    area = models.CharField(max_length = 100, verbose_name = 'Area')
    sueldo = models.FloatField(verbose_name = 'Sueldo')

class administradores(models.Model):
    id_administrador = models.AutoField(primary_key = True)
    id_empleado = models.ForeignKey(empleados, on_delete=models.PROTECT, verbose_name = 'Empleado')
    nom_usuario = models.CharField(max_length=20, verbose_name = 'Nombre de usuario')
    contra = models.CharField(max_length=20, verbose_name = 'Contraseña')
