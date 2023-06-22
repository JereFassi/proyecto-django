from django import forms
# from django.core.validators import validate_email
from integrador.form_validators import *
from .models import Cliente, Domicilio, OrdenTrabajo

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields='__all__'
        exclude=('baja','fecha_baja',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Cliente'}),
            'apellido': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Cliente'}),
            # 'tipo_dni': forms.NumberInput(attrs={'class':'form-select'}),
            'dni': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'fecha_alta': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            # 'vendedor_id': forms.TextInput(attrs={'class':'form-select'})
        }
        error_messages = {
            
        }

    DOC_TIPO = [
        (1,'DNI'),
        (2,'CUIT'),
        (3,'CUIL'),
    ]

    tipo_dni = forms.ChoiceField(
        label = 'Tipo DNI',
        choices = DOC_TIPO,
        initial = 1,
        widget = forms.Select(attrs={'class':'form-select'})
    )

class DomicilioForm(forms.ModelForm):
    class Meta:
        model=Domicilio
        fields='__all__'
        exclude=('cliente_id',)
        widgets = {
            'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese calle y número'}),
            'localidad':forms.TextInput(attrs={'class':'form-control','placeholder':'ej: Bahía Blanca'}),
            'codigo_postal':forms.TextInput(attrs={'class':'form-control'}),
            'latitud':forms.TextInput(attrs={'class':'form-control','editable':'false'}),
            'longitud':forms.TextInput(attrs={'class':'form-control','editable':'false'}),
        }
        error_messages = {
            'codigo_postal' :{
                'required':'Formato numérico XXXX'
            }
        }

    FUENTES = (
        ('',' - Seleccione - '),
        ('https://geocode.maps.co/search?','Geocode'),
        ('https://nominatim.openstreetmap.org/search?format=json','Openstreetmap'),
    )

    PAISES = (
        ('AR','Argentina'),
        ('BR','Brasil'),
    )

    PROVINCIAS = (
        (1, 'Buenos Aires'),
        (2, 'Córdoba'),
        (3, 'Santa Fe'),
        (4, 'C.A.B.A.'),
    )

    fuente = forms.ChoiceField(
        label = 'Fuente de consulta',
        choices = FUENTES,
        initial = 1,
        widget = forms.Select(attrs={'class': 'form-control', 'placeholder':'',})
    )

    pais = forms.ChoiceField(
        label = 'País',
        choices = PAISES,
        initial = 1,
        widget = forms.Select(attrs={'class': 'form-select', 'placeholder':'',})
    )

    provincia = forms.ChoiceField(
        label = 'Provincia',
        choices = PROVINCIAS,
        initial = 1,
        widget = forms.Select(attrs={'class': 'form-select', 'placeholder':'',})
    )

class OrdenTrabajoForm(forms.ModelForm):
    
    class Meta:
        model=OrdenTrabajo
        fields='__all__'
        exclude = ('domicilio_id', 'tecnico_id')
        widgets = {
            
        }
        error_messages = {
            
        }
