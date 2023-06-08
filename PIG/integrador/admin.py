from django.contrib import admin
from .models import Empleado, Domicilio, Tecnico, Vendedor, Servicio, OrdenTrabajo, Usuario
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# Register your models here.

# Registro el modelo Empleado para usarlo en el administrador con la vista predeterminada 
#class EmpleadoAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Empleado)

#Para configurar la vista del administrador y los modelos
class G3AdminSite(admin.AdminSite):
    site_header = 'Administracion G3 Internet'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio'
    empty_value_display = 'No hay datos para visualizar'

class OrdenTrabajoInline(admin.TabularInline):
    model = OrdenTrabajo

class OrdenTrabajoAdmin(admin.ModelAdmin):
    pass
    
class VendedorAdmin(admin.ModelAdmin):
    list_display=('apellido', 'legajo',)
    list_editable = ()
    list_filter = ('dni',)
    search_fields = ('nombre','apellido')

    def get_queryset(self, request):
        query = super(VendedorAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query
    
class TecnicoAdmin(admin.ModelAdmin):
    list_display=('apellido', 'legajo',)
    list_editable = ()
    list_filter = ('dni',)
    search_fields = ('nombre','apellido')
    inlines = [
        OrdenTrabajoInline,
    ]

    def get_queryset(self, request):
        query = super(TecnicoAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "provincia":
            kwargs["queryset"] = Domicilio.objects.filter(provincia=self.provincia)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    
class ServicioAdmin(admin.ModelAdmin):
    list_display=('descripcion',)
#modificar listados de foreingkey para que solo muestre los que no estan de baja
    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
        #if db_field.name == "categoria":
            #kwargs["queryset"] = ModelXX.objects.filter(baja=False)
        #return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
sitio_admin = G3AdminSite(name='g3admin')
sitio_admin.register(Vendedor,VendedorAdmin)
sitio_admin.register(Tecnico,TecnicoAdmin)
sitio_admin.register(Servicio,ServicioAdmin)
sitio_admin.register(OrdenTrabajo,OrdenTrabajoAdmin)
sitio_admin.register(Usuario,UserAdmin)
sitio_admin.register(Group,GroupAdmin)