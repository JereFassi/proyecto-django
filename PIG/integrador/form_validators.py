from django.forms import ValidationError
import re

def only_letters(value):
    if any(char.isdigit() for char in value):
        # raise ValidationError('El nombre no puede contener números. %(valor)s', code = 'Invalid', params = {'valor': value})
        raise ValidationError('El nombre no puede contener números.', code = 'Invalid', params = {'valor': value})
    
def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value