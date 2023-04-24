from django import forms
from django.forms import ValidationError
from django.core.validators import validate_email

def only_letters(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s', code = 'Invalid', params = {'valor': value})

class ClienteForm(forms.Form):

    nombre_y_apellido = forms.CharField(
        label = 'Nombre y Apellido',
        max_length = 256,
        validators=(only_letters,),
        widget = forms.TextInput(attrs={"class": "form-control", 'placeholder':'Homero Simpson'})
    )

    dni = forms.IntegerField(
        label = 'Documento de Identidad',
        widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'12345678'})
    )

    email = forms.EmailField(
        label = 'Email',
        max_length = 128,
        validators = (validate_email,),
        widget = forms.TextInput(attrs={'class':'form-control','type':'email', 'placeholder':'pig@cac.com.ar'})
    )

    telefono = forms.IntegerField(
        label = 'Telefono',
        widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'+54 9 291 425262'})
    )