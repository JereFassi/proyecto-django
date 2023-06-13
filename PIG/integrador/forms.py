from django import forms
# from django.core.validators import validate_email
from integrador.form_validators import *
from .models import Cliente, Domicilio


class ClienteForm(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields='__all__'
        widgets = {
            
        }
        error_messages = {
            
        }

class DomicilioForm(forms.ModelForm):
    class Meta:
        model=Domicilio
        fields='__all__'
        # exclude=('cliente_id','servicio_id',)
        exclude=('cliente_id',)
        widgets = {
            'direccion' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese calle y número'}),
            'localidad' :forms.TextInput(attrs={"class": "form-control", 'placeholder':'ej: Bahía Blanca'})
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

    
    fuente = forms.ChoiceField(
        label = 'Fuente de consulta',
        choices = FUENTES,
        initial = 1,
        widget = forms.Select(attrs={"class": "form-control", 'placeholder':'',})
    )

    pais = forms.ChoiceField(
        label = 'País',
        choices = PAISES,
        initial = 1,
        widget = forms.Select(attrs={"class": "form-control", 'placeholder':'',})
    )
