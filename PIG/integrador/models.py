from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    #domicilio = models.CharField(max_length=100,verbose_name='Domicilio')
    DOC_TIPO = [
        (1,'DNI'),
        (2,'CUIT'),
        (3, 'CUIL'),]
    tipo_dni = models.IntegerField(choices=DOC_TIPO, verbose_name='Tipo de documento')
    dni = models.IntegerField(verbose_name="Documento")
    email = models.EmailField(max_length=150)
    baja=models.BooleanField(default=False)

    class Meta:
        abstract = True

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

PROVINCIA=[
        (1, 'Buenos Aires'),
        (2, 'Córdoba'),
        (3, 'Santa Fe'),
        (4, 'C.A.B.A.'),
    ]

class Empleado(Persona):
    legajo = models.IntegerField(verbose_name='Legajo')
    #CATEGORIA = [
        #(1,'Vendedor'),
        #(2,'Supervisor'),]
    #categoria = models.IntegerField(choices = CATEGORIA, verbose_name = 'Categoría')
    
    def __str__(self):
        return f"{self.legajo} - {self.apellido}"
    
    def soft_delete(self):
        self.baja = True
        super().save()
    
    def restore(self):
        self.baja = False
        super().save()
    
    class Meta():
        verbose_name_plural = 'empleados'

class Vendedor(Empleado):
    comision = models.IntegerField(null = True, verbose_name = 'Comisión de Venta')
    
    class Meta():
        verbose_name_plural = 'vendedores'

class Tecnico(Empleado):
    provincia = models.IntegerField(choices=PROVINCIA)

class Supervisor(Empleado):
    pass

class Cliente(Persona):
    #SERVICIOS = [
        #(1,'Internet 300'),
        #(2,'Internet 500'),
        #(3,'Internet 1000'),
        #(4, 'Pymes 1000'),]
    #tipo_servicio = models.IntegerField(choices=SERVICIOS)
    fecha_alta = models.DateField(verbose_name='Fecha de Alta')
    fecha_baja = models.DateField(null=True, blank=True)
    vendedor_id = models.ForeignKey(Vendedor, on_delete=models.CASCADE, verbose_name='Vendedor asignado')
    
    def __str__(self):
        return f"{self.apellido} - {self.dni}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'clientes'

class Servicio(models.Model):
    descripcion = models.CharField(max_length=50, verbose_name='Tipo de servicio')
    downstream_mv = models.IntegerField(validators=[MinValueValidator(-5),
                                       MaxValueValidator(10)],default=0)
    downstream_snr = models.IntegerField(validators=[MinValueValidator(33),
                                       MaxValueValidator(40)],default=37)
    upstream_mv = models.IntegerField(validators=[MinValueValidator(40),
                                       MaxValueValidator(50)],default=45)
    
    def __str__(self):
        return f"{self.descripcion}"

class Domicilio(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    servicio_id = models.ManyToManyField(Servicio, verbose_name='Tipo de servicio',blank=True, null=True)
    direccion = models.CharField(max_length=100, verbose_name='Domicilio')
    codigo_postal = models.CharField(max_length=20, verbose_name='Código Postal')
    localidad = models.CharField(max_length=50, verbose_name='Localidad')
    provincia =models.IntegerField(choices=PROVINCIA)
    latitud=models.FloatField(max_length=20, verbose_name='Coordenada Latitud', blank=True, null=True)
    longitud=models.FloatField(max_length=20, verbose_name='Coordenada Longitud', blank=True, null=True)

    def __str__(self):
        return f"{self.direccion} - {self.localidad}"

class OrdenTrabajo(models.Model):
    domicilio_id=models.ForeignKey(Domicilio, on_delete=models.CASCADE, verbose_name='Domicilio de instalación')
    tecnico_id=models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name='Técnico Asignado')
    fecha_instalacion=models.DateField(verbose_name='Fecha de Instalación')
    ESTADO= [
        (1,'Pendiente'),
        (2,'Realizada'),
        (3,'Cancelada'),
        ]
    estado_ot=models.IntegerField(choices=ESTADO, verbose_name='Estado de la Orden de Trabajo')

    def __str__(self):
        return f"{self.tecnico_id} - {self.domicilio_id} - {self.estado_ot}"
    
    class Meta():
        verbose_name_plural = 'Ordenes de Trabajo'