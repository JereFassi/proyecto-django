# Generated by Django 3.2.18 on 2023-06-03 13:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('tipo_dni', models.IntegerField(choices=[(1, 'DNI'), (2, 'CUIT'), (3, 'CUIL')], verbose_name='Tipo de documento')),
                ('dni', models.IntegerField(verbose_name='Documento')),
                ('email', models.EmailField(max_length=150)),
                ('baja', models.BooleanField(default=False)),
                ('fecha_alta', models.DateField(verbose_name='Fecha de Alta')),
                ('fecha_baja', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('tipo_dni', models.IntegerField(choices=[(1, 'DNI'), (2, 'CUIT'), (3, 'CUIL')], verbose_name='Tipo de documento')),
                ('dni', models.IntegerField(verbose_name='Documento')),
                ('email', models.EmailField(max_length=150)),
                ('baja', models.BooleanField(default=False)),
                ('legajo', models.IntegerField(verbose_name='Legajo')),
            ],
            options={
                'verbose_name_plural': 'empleados',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Tipo de servicio')),
                ('downstream_mv', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(10)])),
                ('downstream_snr', models.IntegerField(default=37, validators=[django.core.validators.MinValueValidator(33), django.core.validators.MaxValueValidator(40)])),
                ('upstream_mv', models.IntegerField(default=45, validators=[django.core.validators.MinValueValidator(40), django.core.validators.MaxValueValidator(50)])),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrador.empleado')),
            ],
            options={
                'abstract': False,
            },
            bases=('integrador.empleado',),
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrador.empleado')),
                ('provincia', models.IntegerField(choices=[(1, 'Buenos Aires'), (2, 'Córdoba'), (3, 'Santa Fe')])),
            ],
            options={
                'abstract': False,
            },
            bases=('integrador.empleado',),
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrador.empleado')),
                ('comision', models.IntegerField(null=True, verbose_name='Comisión de Venta')),
            ],
            options={
                'verbose_name_plural': 'vendedores',
            },
            bases=('integrador.empleado',),
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100, verbose_name='Domicilio')),
                ('codigo_postal', models.CharField(max_length=20, verbose_name='Código Postal')),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('provincia', models.IntegerField(choices=[(1, 'Buenos Aires'), (2, 'Córdoba'), (3, 'Santa Fe')])),
                ('latitud', models.FloatField(max_length=20, verbose_name='Coordenada Latitud')),
                ('longitud', models.FloatField(max_length=20, verbose_name='Coordenada Longitud')),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrador.cliente', verbose_name='Cliente')),
                ('servicio_id', models.ManyToManyField(to='integrador.Servicio', verbose_name='Tipo de servicio')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_instalacion', models.DateField(verbose_name='Fecha de Instalación')),
                ('estado_ot', models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Realizada'), (3, 'Cancelada')], verbose_name='Estado de la Orden de Trabajo')),
                ('domicilio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrador.domicilio', verbose_name='Domicilio de instalación')),
                ('tecnico_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrador.tecnico', verbose_name='Técnico Asignado')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='vendedor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrador.vendedor', verbose_name='Vendedor asignado'),
        ),
    ]
