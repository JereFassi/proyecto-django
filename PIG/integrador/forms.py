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
        error_messages = {'required': 'Por favor completa el campo'},
        widget = forms.TextInput(attrs={'class':'form-control','type':'email', 'placeholder':'pig@cac.com.ar', "onkeyup": "formValidate()"})
    )

    telefono = forms.IntegerField(
        label = 'Telefono',
        widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':'+54 9 291 425262', "onkeyup": "formValidate()"})
    )