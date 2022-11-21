from ast import Return, Str
from enum import auto

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .forms import (Autor_form, Copias_libros_form, Editorial_form,
                    Empleados_form, Lector_form, Libro_form, Prestamo_form,
                    Sucursal_form)
from .models import (administradores, autores, copias_libros, editoriales,
                     empleados, lectores, libros, prestamos, sucursales)


#LOGIN
def ingresar(request):
    if request.POST:
        usuario = request.POST['usuario']
        cont = request.POST['contra']

        user = authenticate(request, username = usuario, password = cont)

        if user is None:
            print('none')
            return render(request, 'paginas/login.html', {'error':'Usuario o contraseña incorrectos'})
        else:
            print('se')
            login(request, user)
            return redirect('inicio')


    return render(request, 'paginas/login.html')
    

#PAGINA DE INICIO
def inicio(request):
    return render(request, 'paginas/inicio.html')

#-----------------------------------------------------ADMINISTRADORES
def mostrar_administradores(request):
    lista_administradores = list(administradores.objects.raw('SELECT * FROM LIBRERIA_ADMINISTRADORES'))
    return render(request, 'administradores/index.html', {'administradores': lista_administradores})

#-----------------------------------------------------PAGINAS DE AUTORES-----------------------------------------------------
#MOSTRAR LA LISTA DE AUTORES
def mostrar_autores(request):
    lista_autores = list(autores.objects.raw('SELECT * FROM LIBRERIA_AUTORES ORDER BY ID_AUTOR'))
    return render(request, 'autores/index.html', {'autores': lista_autores})

#CREAR UN AUTOR
def crear_autor(request):
    if request.POST:
        formulario = Autor_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('autores')

    return render(request, 'autores/crear.html', {'formulario': Autor_form})

def editar_autor(request, id):
    #SE OBTIENE EL LIBRO Y EL FORMULARIO DE ESTE
    autor = autores.objects.get(id_autor = id)
    formulario = Autor_form(request.POST or None, instance=autor)

    #ENVIO DE FORMULARIO GUARDADO
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('autores')

    return render(request, 'autores/editar.html', {'formulario': formulario})

def eliminar_autor(request, id):
    autor = autores.objects.get(id_autor = id)
    autor.delete()
    return redirect('autores')

#-----------------------------------------------------PAGINAS DE editoriales-----------------------------------------------------
def mostrar_editoriales(request):
    lista_editoriales = list(editoriales.objects.raw('SELECT * FROM LIBRERIA_EDITORIALES ORDER BY ID_EDITORIAL'))
    return render(request, 'editoriales/index.html', {'editoriales': lista_editoriales})

def crear_editorial(request):
    if request.POST:
        formulario = Editorial_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('editoriales')

    return render(request, 'editoriales/crear.html', {'formulario': Editorial_form})

def editar_editorial(request, id):
    #SE OBTIENE EL LIBRO Y EL FORMULARIO DE ESTE
    editorial = editoriales.objects.get(id_editorial = id)
    formulario = Editorial_form(request.POST or None, instance=editorial)

    #ENVIO DE FORMULARIO GUARDADO
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('editoriales')

    return render(request, 'editoriales/editar.html', {'formulario': formulario})

def eliminar_editorial(request, id):
    editorial = editoriales.objects.get(id_editorial = id)
    editorial.delete()
    return redirect('editoriales')


#-----------------------------------------------------PAGINAS DE LIBROS-----------------------------------------------------
#MOSTAR LA LISTA DE LIBROS
def mostrar_libros(request):
    LIBROS = list(libros.objects.raw('SELECT * FROM LIBRERIA_LIBROS ORDER BY ID_LIBRO'))
    return render(request, 'libros/index.html', {'libros': LIBROS})

#CREAR UN LIBRO
def crear_libro(request):
    lista_autores = list(autores.objects.raw('SELECT * FROM LIBRERIA_AUTORES'))
    lista_editoriales = list(editoriales.objects.raw('SELECT * FROM LIBRERIA_EDITORIALES'))

    if request.method == 'POST':
        formulario = Libro_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('libros')
        
    return render(request, 'libros/crear.html', {'formulario': Libro_form, 'autores': lista_autores, 'editoriales': lista_editoriales})

#EDITAR UN LIBRO
def editar_libro(request, id):
    #SE OBTIENE LAS LISTAS DE AUTORES Y EDITORIALES
    lista_autores = list(autores.objects.raw('SELECT * FROM LIBRERIA_AUTORES'))
    lista_editoriales = list(editoriales.objects.raw('SELECT * FROM LIBRERIA_EDITORIALES'))

    #SE OBTIENE EL LIBRO Y EL FORMULARIO DE ESTE
    libro = libros.objects.get(id_libro = id)
    formulario = Libro_form(request.POST or None, instance=libro)

    #ENVIO DE FORMULARIO GUARDADO
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')

    #SE BUSCA EL AUTOR Y LA EDITORIAL CORRESPONDIENTE
    autor = autores.objects.get(id_autor=libro.autor.id_autor)
    editorial = editoriales.objects.get(id_editorial=libro.editorial.id_editorial)

    return render(request, 'libros/editar.html', {'formulario': formulario, 'autores': lista_autores, 
                'autor':autor, 'editoriales': lista_editoriales, 'editorial':editorial})

#ELIMINAR UN LIBRO
def eliminar_libro(request, id):
    libro = libros.objects.get(id_libro = id)
    libro.delete()
    return redirect('libros')

#BUSCAR UN LIBRO

#-----------------------------------------------------PAGINAS DE LECTORES-----------------------------------------------------
def mostrar_lectores(request):
    lista_lectores = list(lectores.objects.raw('SELECT * FROM LIBRERIA_LECTORES ORDER BY NO_TARJETA'))
    return render(request, 'lectores/index.html', {'lectores': lista_lectores})

def crear_lector(request):
    if request.POST:
        formulario = Lector_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lectores')

    return render(request, 'lectores/crear.html', {'formulario': Lector_form})

def editar_lector(request, id):
    #SE OBTIENE EL LIBRO Y EL FORMULARIO DE ESTE
    lector = lectores.objects.get(no_tarjeta = id)
    formulario = Lector_form(request.POST or None, instance=lector)

    #ENVIO DE FORMULARIO GUARDADO
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('lectores')

    return render(request, 'lectores/editar.html', {'formulario': formulario})

def eliminar_lector(request, id):
    lector = lectores.objects.get(no_tarjeta = id)
    lector.delete()
    return redirect('lectores')

#-----------------------------------------------------PAGINAS DE SUCURSALES-----------------------------------------------------
def mostrar_sucursales(request):
    lista_sucursales = list(sucursales.objects.raw('SELECT * FROM LIBRERIA_SUCURSALES ORDER BY ID_SUCURSAL'))
    return render(request, 'sucursales/index.html', {'sucursales': lista_sucursales})

def crear_sucursal(request):
    if request.POST:
        formulario = Sucursal_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sucursales')

    return render(request, 'sucursales/crear.html', {'formulario': Sucursal_form})

def editar_sucursal(request, id):
    #SE OBTIENE EL LIBRO Y EL FORMULARIO DE ESTE
    sucursal = sucursales.objects.get(id_sucursal = id)
    formulario = Sucursal_form(request.POST or None, instance=sucursal)

    #ENVIO DE FORMULARIO GUARDADO
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('sucursales')

    return render(request, 'sucursales/editar.html', {'formulario': formulario})

def eliminar_sucursal(request, id):
    sucursal = sucursales.objects.get(id_sucursal = id)
    sucursal.delete()
    return redirect('sucursales')

#-----------------------------------------------------PAGINAS DE PRESTAMOS-----------------------------------------------------
def mostrar_prestamos(request):
    lista_prestamos = list(prestamos.objects.raw('SELECT * FROM LIBRERIA_PRESTAMOS ORDER BY ID_PRESTAMO'))
    return render(request, 'prestamos/index.html', {'prestamos': lista_prestamos})

def crear_prestamo(request):
    if request.POST:
        formulario = Prestamo_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('prestamos')

    lista_sucursales = list(sucursales.objects.raw('SELECT * FROM LIBRERIA_SUCURSALES ORDER BY ID_SUCURSAL'))
    return render(request, 'prestamos/crear.html', {'formulario': Prestamo_form, 'sucursales': lista_sucursales})

def editar_prestamo(request, id):
    #SE OBTIENE EL PRESTAMO POR EDITAR Y EL FORMULARIO DE ESTE
    prestamo = prestamos.objects.get(id_prestamo = id)
    formulario = Prestamo_form(request.POST or None, instance=prestamo)

    #ENVIO DE FORMULARIO GUARDADO
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('prestamos')

    #SE OBTIENE LA SUCURSAL DEL PRESTAMO
    sucursal = sucursales.objects.get(id_sucursal=prestamo.id_sucursal.id_sucursal)

    lista_sucursales = list(sucursales.objects.raw('SELECT * FROM LIBRERIA_SUCURSALES ORDER BY ID_SUCURSAL'))
    return render(request, 'prestamos/editar.html', {'formulario': formulario, 'sucursal': sucursal, 'sucursales': lista_sucursales})

def eliminar_prestamo(request, id):
    prestamo = prestamos.objects.get(id_prestamo = id)
    prestamo.delete()
    return redirect('prestamos')

#-----------------------------------------------------PAGINAS DE COPIAS-----------------------------------------------------
def mostrar_copias(request):
    lista_copias = list(copias_libros.objects.raw('SELECT * FROM LIBRERIA_COPIAS_LIBROS ORDER BY ID'))
    return render(request, 'copias/index.html', {'copias': lista_copias})

def crear_copia(request):
    if request.POST:
        formulario = Copias_libros_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('copias')

    return render(request, 'copias/crear.html', {'formulario': Copias_libros_form})

def editar_copia(request, id):
    #SE OBTIENE EL LIBRO Y EL FORMULARIO DE ESTE
    copia = copias_libros.objects.get(id = id)
    formulario = Copias_libros_form(request.POST or None, instance=copia)

    #ENVIO DE FORMULARIO GUARDADO
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('copias')

    return render(request, 'copias/editar.html', {'formulario': formulario})

def eliminar_copia(request, id):
    copia = copias_libros.objects.get(id = id)
    copia.delete()
    return redirect('copias')

#-----------------------------------------------------PAGINAS DE COPIAS-----------------------------------------------------
def mostrar_empleados(request):
    lista_empleados = list(empleados.objects.raw('SELECT * FROM LIBRERIA_EMPLEADOS ORDER BY ID_EMPLEADO'))
    return render(request, 'empleados/index.html', {'empleados': lista_empleados})

def crear_empleado(request):
    if request.POST:
        formulario = Empleados_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleados')

    return render(request, 'empleados/crear.html', {'formulario': Empleados_form})

def editar_empleado(request, id):
    #SE OBTIENE EL LIBRO Y EL FORMULARIO DE ESTE
    empleado = empleados.objects.get(id_empleado = id)
    formulario = Empleados_form(request.POST or None, instance=empleado)

    #ENVIO DE FORMULARIO GUARDADO
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('empleados')

    return render(request, 'empleados/editar.html', {'formulario': formulario})

def eliminar_empleado(request, id):
    empleado = empleados.objects.get(id_empleado = id)
    empleado.delete()
    return redirect('empleados')