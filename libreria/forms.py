from dataclasses import fields
from pyexpat import model
from statistics import mode
from django import forms
from .models import administradores, autores, copias_libros, editoriales, empleados, lectores, libros, prestamos, sucursales

class Autor_form(forms.ModelForm):
    class Meta:
        model = autores
        fields = ('__all__')

class Editorial_form(forms.ModelForm):
    class Meta:
        model = editoriales
        fields = ('__all__')

class Libro_form(forms.ModelForm):
    class Meta:
        model = libros
        fields = ('__all__')

class Lector_form(forms.ModelForm):
    class Meta:
        model = lectores
        fields = ('__all__')

class Sucursal_form(forms.ModelForm):
    class Meta:
        model = sucursales
        fields = ('__all__')

class Prestamo_form(forms.ModelForm):
    class Meta:
        model = prestamos
        fields = ('__all__')     

class Copias_libros_form(forms.ModelForm):
    class Meta:
        model = copias_libros
        fields = ('__all__')

class Empleados_form(forms.ModelForm):
    class Meta:
        model = empleados
        fields = ('__all__')

class Administradores_form(forms.ModelForm):
    class Meta:
        model = administradores
        fields = ('__all__')
