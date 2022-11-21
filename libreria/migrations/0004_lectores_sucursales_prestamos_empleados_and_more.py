# Generated by Django 4.1.1 on 2022-10-17 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_rename_titulo_libros_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='lectores',
            fields=[
                ('no_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo electronico')),
            ],
        ),
        migrations.CreateModel(
            name='sucursales',
            fields=[
                ('id_sucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='prestamos',
            fields=[
                ('id_prestamo', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio de prestamo')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de finalización de prestamo')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libreria.libros', verbose_name='Libro')),
                ('id_sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libreria.sucursales', verbose_name='Sucursal')),
                ('no_tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libreria.lectores', verbose_name='Lector')),
            ],
        ),
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('area', models.CharField(max_length=100, verbose_name='Area')),
                ('sueldo', models.FloatField(verbose_name='Teléfono')),
                ('id_sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libreria.sucursales', verbose_name='Sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='copias_libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_copias', models.IntegerField(verbose_name='Número de copias')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libreria.libros', verbose_name='Libro')),
                ('id_sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libreria.sucursales', verbose_name='Sucursal')),
            ],
        ),
    ]
