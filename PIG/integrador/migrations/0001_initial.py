# Generated by Django 3.2.18 on 2023-05-31 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('domicilio', models.CharField(max_length=100, verbose_name='Domicilio')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('email', models.EmailField(max_length=150)),
                ('baja', models.BooleanField(default=False)),
                ('legajo', models.IntegerField(verbose_name='Legajo')),
                ('categoria', models.IntegerField(choices=[(1, 'Vendedor'), (2, 'Supervisor')], verbose_name='Categoría')),
                ('comision', models.IntegerField(null=True, verbose_name='Comisión de Venta')),
            ],
            options={
                'verbose_name_plural': 'empleados',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('domicilio', models.CharField(max_length=100, verbose_name='Domicilio')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('email', models.EmailField(max_length=150)),
                ('baja', models.BooleanField(default=False)),
                ('tipo_servicio', models.IntegerField(choices=[(1, 'Internet 300'), (2, 'Internet 500'), (3, 'Internet 1000'), (4, 'Pymes 1000')])),
                ('fecha_alta', models.DateField(verbose_name='Fecha de Alta')),
                ('fecha_baja', models.DateField(blank=True, null=True)),
                ('coordenada_domicilio', models.CharField(max_length=50, verbose_name='Coordenadas domicilio')),
                ('legajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrador.empleado', verbose_name='Vendedor asignado')),
            ],
            options={
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
