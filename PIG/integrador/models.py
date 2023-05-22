from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    dni = models.IntegerField(verbose_name="DNI")
    email = models.EmailField(max_length=150)
    class Meta:
        abstract=True   

  
class Empleado(Persona):
    legajo = models.IntegerField(verbose_name='Legajo')
    CATEGORIA = [
        (1,'Vendedor'),
        (2,'Supervisor'),
    ]
    categoria = models.IntegerField(choices=CATEGORIA, verbose_name='Categoría')
    comision = models.IntegerField(null=True, verbose_name='Comisión de Venta')
    
    def __str__(self):
        return f"{self.legajo} - {self.apellido} {self.nombre}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'empleados'


class Cliente(Persona):
    SERVICIOS = [
        (1,'Internet 300'),
        (2,'Internet 500'),
        (3,'Internet 1000'),
        (4, 'Pymes 1000'),
    ]
    tipo_servicio = models.IntegerField(choices=SERVICIOS)
    fecha_alta = models.DateField(verbose_name='Fecha de Alta')
    fecha_baja = models.DateField(verbose_name='Fecha de Baja',null=True,default=None)
    coordenada_domicilio = models.CharField(max_length=50, verbose_name='Coordenadas domicilio')
    legajo=models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_servicio} - {self.nombre} {self.apellido}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()