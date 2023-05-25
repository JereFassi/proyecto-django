# Create your views here.

# framework
import logging
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# app
from integrador.forms import *
from integrador.communications import *
from integrador.maps import *
from .forms import ClienteForm, EmpleadoForm
from .models import Cliente, Empleado
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Q



"""
    CRUD Empleado
"""
def empleado_index(request):
    #queryset
    empleado = Empleado.objects.filter()
    return render(request,'integrador/empleado/index.html',{'empleado':empleado})

def empleado_nuevo(request):
    if(request.method=='POST'):
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleado_index')
    else:
        formulario = EmpleadoForm()
    return render(request,'integrador/empleado/nuevo.html',{'form':formulario})

def empleado_editar(request,id):
    try:
        empleado = Empleado.objects.get(pk = id)
    except Empleado.DoesNotExist:
        return render(request,'error-404.html')

    if(request.method=='POST'):
        formulario = EmpleadoForm(request.POST,instance = empleado)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleado_index')
    else:
        formulario = EmpleadoForm(instance = empleado)
    return render(request,'integrador/empleado/editar.html',{'form':formulario})

def empleado_eliminar(request,id):
    try:
        empleado = Empleado.objects.get(pk = id)
    except Empleado.DoesNotExist:
        return render(request,'error-404.html')
    empleado.soft_delete()
    return redirect('empleado_index')

"""
    CRUD Cliente
"""
def cliente_index(request):
    #queryset
    cliente = Cliente.objects.all()
    return render(request,'integrador/cliente/index.html',{'cliente':cliente})

def cliente_nuevo(request):
    if(request.method=='POST'):
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('cliente_index')
    else:
        formulario = ClienteForm()
    return render(request,'integrador/cliente/nuevo.html',{'form':formulario})

def cliente_editar(request,id):
    try:
        cliente = Cliente.objects.get(pk = id)
    except Cliente.DoesNotExist:
        return render(request,'error-404.html')

    if(request.method=='POST'):
        formulario = ClienteForm(request.POST,instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('cliente_index')
    else:
        formulario = ClienteForm(instance = cliente)
    return render(request,'integrador/cliente/editar.html',{'form':formulario})

def cliente_eliminar(request,id):
    try:
        cliente = Cliente.objects.get(pk = id)
    except Cliente.DoesNotExist:
        return render(request,'error-404.html')
    cliente.soft_delete()
    return redirect('cliente_index')

def get_queryset(request):
        queryset = request.GET.get("buscar")
        cliente=Cliente.objects.filter(baja=False)
        if queryset:
            cliente=Cliente.objects.filter(
                Q(apellido__icontains=queryset)
            )
        return render(request,'integrador/cliente/index.html',{'cliente':cliente}) 
        

logger = logging.getLogger(__name__)

def index(request):

    context = {}

    if(request.method=="POST"):
        contacto_form = ContactoForm(request.POST)
        if(contacto_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos correctamente')          
            # acción para tomar los datos del formulario
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        contacto_form = ContactoForm()
    
    context.update({
        'contacto_form': contacto_form,
    })

    return render(request,'integrador/index.html', context)

def clientes(request):
    
    context = {}
    mensaje = None

    if(request.method=='POST'):
        cliente_form = ClientesForm(request.POST)
        if(cliente_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos correctamente')          
            # acción para tomar los datos del formulario
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        cliente_form = ClientesForm()
    
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
            fuente = domicilio_form.cleaned_data['fuente']
            data = consulta_geodecode(fuente, domicilio_datos)
            if data != None:
                mapa_html = generar_mapa_html(data)
            else:
                f"<h4> No se pudo generar el mapa </h4>"
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

def contacto(request):
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
                messages.info(request, "Datos enviados")
    else:
        contacto_form = ContactoForm()
    return render(request,'integrador/index.html', {'contacto_form': contacto_form})

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
