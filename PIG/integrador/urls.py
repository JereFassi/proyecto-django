
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('inicio_empleado/', views.index, name='inicio_empleado'),
    path('cliente/', views.cliente_index,name='cliente_index'),
    path('cliente/buscar/', views.get_queryset,name='buscar'),
    path('cliente/nuevo/', views.cliente_nuevo,name='cliente_nuevo'),
    path('cliente/editar/<int:id>', views.cliente_editar,name='cliente_editar'),
    path('cliente/eliminar/<int:id>', views.cliente_eliminar,name='cliente_eliminar'),

    path('domicilio/', views.domicilio, name='domicilio'),  
    path('domicilio/<int:cliente_id>', views.domicilio_cliente, name='domicilio_cliente'),
    path('geo/', views.geo_localizacion, name='geo-localizacion'),

    path('servicioview/', views.ServicioListView.as_view(),name='servicio'),

    path('ordentrabajoview/', views.OrdenTrabajoListView.as_view(),name='ordentrabajo'),
    path('ordentrabajoedit/<int:pk>', views.OrdenTrabajoUpdateView.as_view(),name='ordentrabajoedit'),

]

