from django import forms
# from django.core.validators import validate_email
from integrador.form_validators import *

class ClienteForm(forms.Form):

    nombre_y_apellido = forms.CharField(
        label = 'Nombre y Apellido',
        max_length = 256,
        validators=(only_letters,),
        widget = forms.TextInput(attrs={"class": "form-control", 'placeholder':'Homero Simpson', "onkeyup": "formValidate()"})
    )

    dni = forms.IntegerField(
        label = 'Documento de Identidad',
        widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'12345678', "onkeyup": "formValidate()"})
    )

    email = forms.EmailField(
        label = 'Email',
        max_length = 128,
        validators = (validate_email,),
        error_messages = {'required': 'Por favor complete el campo'},
        widget = forms.TextInput(attrs={'class':'form-control','type':'email', 'placeholder':'pig@cac.com.ar', "onkeyup": "formValidate()"})
    )

    telefono = forms.IntegerField(
        label = 'Telefono',
        widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'+54 9 291 425262', "onkeyup": "formValidate()"})
    )

class DomicilioForm(forms.Form):

    FUENTES = (
        ('',' - Seleccione - '),
        ('https://geocode.maps.co/search?','Geocode'),
        ('https://nominatim.openstreetmap.org/search?format=json','Openstreetmap'),
    )

    PAISES = (
        ('',' - Seleccione - '),
        ('AR','Argentina'),
        ('BR','Brasil'),
        ('PR','Patricio Rey'),
    )

    PROVINCIAS = (
        ('',' - Seleccione - '),
        ('Buenos Aires','Buenos Aires'),
        ('Cordoba','Córdoba'),
        ('La Pampa','La Pampa'),
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

    provincia = forms.ChoiceField(
        label = 'Provincia',
        choices = PROVINCIAS,
        initial = 1,
        widget = forms.Select(attrs={"class": "form-control", 'placeholder':'',})
    )

    codigo_postal = forms.IntegerField(
        label = 'Código Postal',
        widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'ej: 8000', "onkeyup": "formValidate()"})
    )

    ciudad = forms.CharField(
        label = 'Ciudad',
        max_length = 256,
        validators=(),
        widget = forms.TextInput(attrs={"class": "form-control", 'placeholder':'ej: bahia blanca', "onkeyup": "formValidate()"})
    )

    calle = forms.CharField(
        label = 'Calle',
        max_length = 256,
        validators=(),
        widget = forms.TextInput(attrs={"class": "form-control", 'placeholder':'ej: alsina', "onkeyup": "formValidate()"})
    )

    numero = forms.IntegerField(
        label = 'Numero',
        widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'ej: 124', "onkeyup": "formValidate()"})
    )

class ContactoForm(forms.Form):

    nombre_contacto = forms.CharField(
        label = 'Nombre y Apellido',
        widget = forms.TextInput(attrs={'class':'form-control', 'name':'nombre_contacto', 'placeholder':'Nombre para contacto'})
    )

    telefono = forms.IntegerField(
        label = 'Teléfono',
        widget = forms.NumberInput(attrs={'class':'form-control','name':'telefono', 'placeholder':'Teléfono Cód Area XXX y número'})
    )

    email = forms.EmailField(
        label = 'Email',
        widget = forms.EmailInput(attrs={'class':'form-control','name':'email', 'placeholder':'Dirección de Email'})
    )