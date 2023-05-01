# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from integrador.forms import *
from integrador.communications import *
from integrador.maps import *

def index(request):

    context = {}

    return render(request,'integrador/index.html', context)

def cliente(request):
    
    context = {}
    mensaje = None

    if(request.method=='POST'):
        cliente_form = ClienteForm(request.POST)
        if(cliente_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos correctamente')          
            # acción para tomar los datos del formulario
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        cliente_form = ClienteForm()
    
    context.update({
        'cliente_form': cliente_form,
        'mensaje': mensaje
    })

    return render(request,'integrador/form-cliente.html', context)

def domicilio(request):
    
    context = {}
    mensaje = None
    data = None
    mapa_html = None

    if(request.method=='POST'):
        domicilio_form = DomicilioForm(request.POST)
        if(domicilio_form.is_valid()):
            messages.success(request,'Hemos recibido tus datos correctamente')
            # acción para tomar los datos del formulario
            domicilio_datos = {
                # "street": f"{domicilio_form.cleaned_data['numero']} {domicilio_form.cleaned_data['calle']}",
                "street": f"{domicilio_form.cleaned_data['calle']} {domicilio_form.cleaned_data['numero']}",
                "city": domicilio_form.cleaned_data['ciudad'],
                "state": domicilio_form.cleaned_data['provincia'],
                "country": domicilio_form.cleaned_data['pais'],
                "postalcode": domicilio_form.cleaned_data['codigo_postal'],
            }
            data = consulta_geodecode(domicilio_datos)
            mapa_html = generar_mapa_html(data)
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        domicilio_form = DomicilioForm()
    
    context.update({
        'domicilio_form': domicilio_form,
        'mensaje': mensaje,
        'data': data,
        'mapa': mapa_html
    })

    return render(request,'integrador/form-domicilio.html', context)

def geo_localizacion(request):
    
    context = {}

    return render(request,'integrador/form-geo-localizacion.html', context)

def dashboard(request):
    
    context = {}

    return render(request,'integrador/dashboard.html', context)

def forms(request):
    
    context = {}

    return render(request,'integrador/forms.html', context)

def tables(request):
    
    context = {}

    return render(request,'integrador/tables.html', context)

def charts(request):
    
    context = {}

    return render(request,'integrador/charts.html', context)

def icons(request):
    
    context = {}

    return render(request,'integrador/icons.html', context)

def ui_buttons(request):
    
    context = {}

    return render(request,'integrador/ui-buttons.html', context)

def ui_badges(request):
    
    context = {}

    return render(request,'integrador/ui-badges.html', context)

def ui_cards(request):
    
    context = {}

    return render(request,'integrador/ui-cards.html', context)

def ui_alerts(request):
    
    context = {}

    return render(request,'integrador/ui-alerts.html', context)

def ui_tabs(request):
    
    context = {}

    return render(request,'integrador/ui-tabs.html', context)

def ui_date_time_picker(request):
    
    context = {}

    return render(request,'integrador/ui-date-time-picker.html', context)

def login(request):

    context = {}

    return render(request,'integrador/login.html', context)

def signup(request):

    context = {}

    return render(request,'integrador/signup.html', context)

def forgot_password(request):

    context = {}

    return render(request,'integrador/forgot-password.html', context)

def blank(request):

    context = {}

    return render(request,'integrador/blank.html', context)

def error_404(request):

    context = {}

    return render(request,'integrador/error-404.html', context)

def error_500(request):

    context = {}

    return render(request,'integrador/error-500.html', context)

def users(request):

    context = {}

    return render(request,'integrador/users.html', context)

def roles(request):

    context = {}

    return render(request,'integrador/roles.html', context)

def permissions(request):

    context = {}

    return render(request,'integrador/permissions.html', context)

def settings(request):

    context = {}

    return render(request,'integrador/settings.html', context)
