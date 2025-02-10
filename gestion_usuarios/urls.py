from django.urls import path
from .views import *

urlpatterns = [
    ####--------Usuarios--------####
    path("listar_usuarios", ListaUsuario.as_view(), name='listar_usuarios'),
    path("registrar_usuario", CrearUsuario.as_view(), name='registrar_usuario'),
    path("actualizar_usuario/<int:pk>/", ActualizarUsuario.as_view(), name='actualizar_usuario'),
    path("detalle_usuario/<int:pk>/", VistaUsuario.as_view(), name='detalle_usuario'),
    path("eliminar_usuario/<int:pk>/", EliminarUsuario.as_view(), name='eliminar_usuario'),  
    
    ####--------Roles--------####
    path("listar_roles", ListaRoles.as_view(), name='listar_roles'),
    path("registrar_rol", CrearRol.as_view(), name='registrar_rol'),
    path("actualizar_rol/<int:pk>/", ActualizarRol.as_view(), name='actualizar_rol'),
    path("eliminar_rol/<int:pk>/", EliminarRol.as_view(), name='eliminar_rol'),  
]