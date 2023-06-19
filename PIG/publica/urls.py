from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('acceso_empleados/', auth_views.LoginView.as_view(
        template_name='publica/login.html',
        extra_context={'variable':'Empleados'},
    ), name='acceso'),
    path('accounts/logout/',auth_views.LogoutView.as_view(
        template_name='integrador/base_integrador',
    ), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url="/"), name='password_change'), 
    path('accounts/', include('django.contrib.auth.urls')),
]