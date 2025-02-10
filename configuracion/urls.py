"""configuracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from gestion_usuarios.views import Login, Inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingresar/', Login.as_view(), name='login'),  # Ruta para el login
    path('inicio/', Inicio.as_view(), name='inicio'),  # Ruta para la página de inicio
    path('', RedirectView.as_view(url='ingresar/')),  # Redirige la ruta raíz a la página de login
    path('gestion_usuarios/', include('gestion_usuarios.urls')),
    path('gestion_cursos/', include('gestion_cursos.urls')),
]
