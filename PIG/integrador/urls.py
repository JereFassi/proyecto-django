
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('inicio_empleado/', views.index, name='inicio_empleado'),
    path('cliente/', views.cliente_index,name='cliente_index'),
    path('cliente/nuevo/', views.cliente_nuevo,name='cliente_nuevo'),
    path('cliente/editar/<int:id>', views.cliente_editar,name='cliente_editar'),
    path('cliente/eliminar/<int:id>', views.cliente_eliminar,name='cliente_eliminar'),
      
    path('domicilio/', views.domicilio, name='domicilio'),
    path('geo/', views.geo_localizacion, name='geo-localizacion'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('forms/', views.forms, name='forms'),
    path('tables/', views.tables, name='tables'),
    path('charts/', views.charts, name='charts'),
    path('icons/', views.icons, name='icons'),
    path('ui-buttons/', views.ui_buttons, name='ui-buttons'),
    path('ui-badges/', views.ui_badges, name='ui-badges'),
    path('ui-cards/', views.ui_cards, name='ui-cards'),
    path('ui-alerts/', views.ui_alerts, name='ui-alerts'),
    path('ui-tabs/', views.ui_tabs, name='ui-tabs'),
    path('ui-date-time-picker/', views.ui_date_time_picker, name='ui-date-time-picker'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('blank/', views.blank, name='blank'),
    path('error-404/', views.error_404, name='error-404'),
    path('error-500/', views.error_500, name='error-500'),
    path('users/', views.users, name='users'),
    path('roles/', views.roles, name='roles'),
    path('permissions/', views.permissions, name='permissions'),
    path('settings/', views.settings, name='settings'),

    path('servicioview/', views.ServicioListView.as_view(),name='servicio'),

    path('ordentrabajoview/', views.OrdenTrabajoListView.as_view(),name='ordentrabajo'),
    path('ordentrabajoedit/<int:pk>', views.OrdenTrabajoUpdateView.as_view(),name='ordentrabajoedit'),

]

