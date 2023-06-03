from django import forms
# from django.core.validators import validate_email
from integrador.form_validators import *

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

    mensaje = forms.CharField(
        label = 'Mensaje',
        max_length = 1024,
        widget = forms.Textarea(
            attrs = {'class': 'form-control',
                     'rows': 5,
                     'placeholder':'Gracias por su tiempo...',
                    #  'onkeyup': 'formValidate()'
            })
    )