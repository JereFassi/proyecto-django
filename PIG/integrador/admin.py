from django.contrib import admin
from .models import Empleado, Cliente

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


class ClienteAdmin(admin.ModelAdmin):
    list_display=('apellido', 'domicilio','tipo_servicio',)
    list_editable = ()
    list_filter = ('dni',)
    search_fields = ('nombre','apellido')
    
    def get_queryset(self, request):
        query = super(ClienteAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query

class EmpleadoAdmin(admin.ModelAdmin):
    pass
#modificar listados de foreingkey para que solo muestre los que no estan de baja
    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
        #if db_field.name == "categoria":
            #kwargs["queryset"] = ModelXX.objects.filter(baja=False)
        #return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
sitio_admin = G3AdminSite(name='g3admin')
sitio_admin.register(Cliente,ClienteAdmin)
sitio_admin.register(Empleado,EmpleadoAdmin)