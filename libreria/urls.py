from django.urls import path
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #LOGIN
    path('', views.ingresar, name='login'),
    
    #PAGINA DE INICIO
    path('inicio', views.inicio, name='inicio'),

    #ADMINISTRADORES
    path('administradores', views.mostrar_administradores, name = 'administradores'),

    #REPORTES
    path('reportes', views.mostrar_reporte1, name = 'reporte1'),

    #AUTORES
    path('autores', views.mostrar_autores, name = 'autores'),
    path('autores/crear', views.crear_autor, name = 'crear_autor'),
    path('autores/editar/<int:id>', views.editar_autor, name = 'editar_autor'),
    path('eliminar_autor/<int:id>', views.eliminar_autor, name = 'eliminar_autor'),

    #EDITORIALES    
    path('editoriales', views.mostrar_editoriales, name = 'editoriales'),
    path('editoriales/crear', views.crear_editorial, name = 'crear_editorial'),
    path('editoriales/editar/<int:id>', views.editar_editorial, name = 'editar_editorial'),
    path('eliminar_editoriale/<int:id>', views.eliminar_editorial, name = 'eliminar_editorial'),

    #LIBROS
    path('libros', views.mostrar_libros, name = 'libros'),
    path('libros/crear', views.crear_libro, name = 'crear_libro'),
    path('libros/edita/<int:id>', views.editar_libro, name = 'editar_libro'),
    path('eliminar_libro/<int:id>', views.eliminar_libro, name = 'eliminar_libro'),

    #LECTORES
    path('lectores', views.mostrar_lectores, name = 'lectores'),
    path('lectores/crear', views.crear_lector, name = 'crear_lector'),
    path('lectores/edita/<int:id>', views.editar_lector, name = 'editar_lector'),
    path('eliminar_lector/<int:id>', views.eliminar_lector, name = 'eliminar_lector'),

    #SUCURSALES
    path('sucursales', views.mostrar_sucursales, name = 'sucursales'),
    path('sucursales/crear', views.crear_sucursal, name = 'crear_sucursal'),
    path('sucursales/edita/<int:id>', views.editar_sucursal, name = 'editar_sucursal'),
    path('eliminar_sucursal/<int:id>', views.eliminar_sucursal, name = 'eliminar_sucursal'),

    #PRESTAMOS
    path('prestamos', views.mostrar_prestamos, name = 'prestamos'),
    path('prestamos/crear', views.crear_prestamo, name = 'crear_prestamo'),
    path('prestamos/edita/<int:id>', views.editar_prestamo, name = 'editar_prestamo'),
    path('eliminar_prestamo/<int:id>', views.eliminar_prestamo, name = 'eliminar_prestamo'),
    path('prestamos/prestamo_activo', views.prestamo_activo, name = 'prestamo_activo'),
    path('prestamos/agregar_libro_prestamo/<int:id_prestamo>/<int:id_libro>', views.agregar_libro_prestamo, name='agregar_libro_prestamo'),
    path('prestamos/finalizar<int:id_prestamo>', views.finalizar_prestamo, name='finalizar_prestamo'),
    
    #COPIAS LIBROS
    path('copias', views.mostrar_copias, name = 'copias'),
    path('copias/crear', views.crear_copia, name = 'crear_copia'),
    path('copias/edita/<int:id>', views.editar_copia, name = 'editar_copia'),
    path('eliminar_copias/<int:id>', views.eliminar_copia, name = 'eliminar_copia'),

    #EMPLEADOS
    path('empleados', views.mostrar_empleados, name = 'empleados'),
    path('empleados/crear', views.crear_empleado, name = 'crear_empleado'),
    path('empleados/edita/<int:id>', views.editar_empleado, name = 'editar_empleado'),
    path('eliminar_empleado/<int:id>', views.eliminar_empleado, name = 'eliminar_empleado'),
    path('empleados/aumentar_empleado<int:id_empleado>', views.aumentar_empleado, name='aumentar_empleado'),

]

urlpatterns += staticfiles_urlpatterns()