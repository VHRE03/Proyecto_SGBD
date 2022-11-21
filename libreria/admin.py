from django.contrib import admin
from .models import autores, lectores, prestamos, sucursales
from .models import editoriales
from .models import libros
# Register your models here.

admin.site.register(autores)
admin.site.register(editoriales)
admin.site.register(libros)
admin.site.register(lectores)
admin.site.register(sucursales)
admin.site.register(prestamos)