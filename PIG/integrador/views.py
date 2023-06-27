# Create your views here.

# framework
import logging
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# app
from integrador.forms import *
from integrador.communications import *
from integrador.maps import *
from .forms import ClienteForm
from .models import Cliente, Servicio, OrdenTrabajo, Tecnico
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


"""
    CRUD Cliente
"""
@login_required
@permission_required('integrador.view_cliente', login_url='/acceso_empleados')
def cliente_index(request):
    #queryset
        cliente = Cliente.objects.filter(baja=False)
        return render(request,'integrador/cliente/index.html',{'cliente':cliente})

@login_required
@permission_required('integrador.add_cliente', login_url='/acceso_empleados')
def cliente_nuevo(request):
    if(request.method=='POST'):
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            cliente = formulario.save()
            return redirect('domicilio_cliente',cliente.id)
    else:
        formulario = ClienteForm()
    return render(request,'integrador/cliente/nuevo.html',{'form':formulario})

@login_required
@permission_required('integrador.change_cliente', login_url='/acceso_empleados')
def cliente_editar(request,id):
    try:
        cliente = Cliente.objects.get(pk = id)
    except Cliente.DoesNotExist:
        return render(request,'error-404.html')

    if(request.method=='POST'):
        formulario = ClienteForm(request.POST,instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('domicilio_cliente',cliente.id)
    else:
        formulario = ClienteForm(instance = cliente)
    return render(request,'integrador/cliente/editar.html',{'form':formulario})

@login_required
@permission_required('integrador.delete_cliente', login_url='/acceso_empleados')
def cliente_eliminar(request,id):
    try:
        cliente = Cliente.objects.get(pk = id)
    except Cliente.DoesNotExist:
        return render(request,'error-404.html')
    cliente.soft_delete()
    return redirect('cliente_index')

def get_queryset(request):
    queryset = request.GET.get('buscar')
    if queryset:
        cliente=Cliente.objects.filter(
            Q(apellido__icontains=queryset)
        )
    else:
        cliente=Cliente.objects.filter(baja=False)
    return render(request,'integrador/cliente/index.html',{'cliente':cliente}) 
        

logger = logging.getLogger(__name__)

    
@login_required
def index(request):

    context = {}

    return render(request,'integrador/index.html', context)

@login_required
@permission_required('integrador.add_domicilio', login_url='/acceso_empleados')
def domicilio_cliente(request, cliente_id):
    
    context = {}

    if(request.method=='POST'):
        messages.error(request,'Revisar circuito de Alta Cliente')
    else:
        domicilio_form = DomicilioForm()
    
    context.update({
        'domicilio_form': domicilio_form,
        'cliente_id': cliente_id,
    })

    return render(request,'integrador/form-domicilio.html', context)

@login_required
@permission_required('integrador.add_domicilio', login_url='/acceso_empleados')
def domicilio(request):
    
    context = {}
    mensaje = None
    data = None
    mapa_html = None

    if(request.method=='POST'):
        domicilio_form = DomicilioForm(request.POST)
        if(domicilio_form.is_valid()):
            messages.success(request,'Domicilio válido para realizar instalación')
            # acción para tomar los datos del formulario

            cliente_id = domicilio_form.data['cliente_id']
            try:
                cliente = Cliente.objects.get(pk = cliente_id)
            except Cliente.DoesNotExist:
                return render(request,'error-404.html')

            num_provincia=domicilio_form.cleaned_data['provincia']
            if num_provincia==1 or num_provincia==4:
               num_provincia='buenos aires',
            elif num_provincia==2:
               num_provincia='cordoba',
            elif num_provincia==3:
               num_provincia='santa fe'

            domicilio_datos = {
                "street": f"{domicilio_form.cleaned_data['direccion']}",
                "city": domicilio_form.cleaned_data['localidad'],
                "state": num_provincia,
                "country": 'AR',
                "postalcode": domicilio_form.cleaned_data['codigo_postal'],
            }
            fuente = 'Geocode'
            data = consulta_geodecode(fuente, domicilio_datos)
            if data != None:
                mapa_html = generar_mapa_html(data)
                
            else:
                f"<h4> No se pudo generar el mapa </h4>"

            domicilio = domicilio_form.save(commit=False)
            
            domicilio.cliente_id_id = cliente_id
            
            domicilio.save()

            domicilio_form.save_m2m()

            crear_orden(domicilio)
                   
            redirect('cliente_index')
        else:
            messages.warning(request,'Por favor revisa los datos ingresados')
    else:
        domicilio_form = DomicilioForm()
    
    context.update({
        'domicilio_form': domicilio_form,
        'mensaje': mensaje,
        'data': data,
        'mapa': mapa_html
    })

    return render(request,'integrador/form-domicilio.html', context)

def crear_orden(domicilio):

    tecnico = Tecnico.objects.get(pk = 2)

    nueva_orden = OrdenTrabajo()
    nueva_orden.domicilio_id = domicilio
    nueva_orden.fecha_instalacion = datetime.now()
    nueva_orden.estado_ot = 1
    nueva_orden.tecnico_id = tecnico
    nueva_orden.save()

    return

def geo_localizacion(request):
    
    context = {}

    return render(request,'integrador/form-geo-localizacion.html', context)


class ServicioListView(ListView):
    model = Servicio
    context_object_name = 'servicio'
    template_name= 'integrador/form-domicilio.html'
    queryset= Servicio.objects.all()
    ordering = ['descripcion']
    
    def servicio(request):
        context = {}
        return render(request,'integrador/form-domicilio.html', context)

class OrdenTrabajoListView(LoginRequiredMixin,ListView):
    model = OrdenTrabajo
    context_object_name = 'ordentrabajo'
    template_name= 'integrador/form-ordentrabajo.html'
    queryset= OrdenTrabajo.objects.all()
    ordering = ['tecnico_id']
    login_url = 'acceso'
    
    
    def ordentrabajo(request):
        context = {}
        return render(request,'integrador/form-ordentrabajo.html', context)

class Redirect_PermissionRequiredMixin(object):
    permission_required = None
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms
    
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('acceso')
        return self.url_redirect
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        return  HttpResponseRedirect(self.get_url_redirect())
        

class OrdenTrabajoUpdateView(Redirect_PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = OrdenTrabajo
    form_class = OrdenTrabajoForm
    template_name = 'integrador/form-ordentrabajo-editar.html'
    success_url = reverse_lazy('ordentrabajo')
    success_message = "La orden de trabajo de instalación de fecha %(fecha_instalacion)s ha sido actualizada con éxito"
    permission_required = ('integrador.change_ordentrabajo')
    login_url = 'acceso'
