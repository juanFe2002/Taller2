from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import FormView, CreateView, UpdateView, ListView, TemplateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect




class Login(FormView):
    form_class = LoginForm
    template_name = 'gestion_usuarios/login.html'
    success_url = 'inicio'  # Cambia esto por la URL a la que quieres redirigir después del login

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs) 

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                messages.success(self.request, "Sesión iniciada correctamente.")
                return super().form_valid(form)
            else:
                messages.error(self.request, "El usuario no está activo.")
        else:
            messages.error(self.request, "Usuario o contraseña incorrectos.")
        return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error en el formulario. Inténtalo de nuevo.")
        return super().form_invalid(form)


class Inicio(TemplateView):
    template_name = 'inicio.html'
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(Inicio, self).get(request *args, **kwargs)

######-------Crud del Usuaio-------######
class ListaUsuario(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Usuario
    template_name = 'gestion_usuarios/listado_usuarios.html'
    context_object_name = 'usuarios' 
    permissions = {"any": ('gestion_usuarios.registrar_usuario', 'gestion_usuarios.consultar_usuarios', 'gestion_usuarios.actualizar_usuario', 'gestion_usuarios.eliminar_usuario' , 'gestion_usuarios.detalle_usuario' )}


class VistaUsuario(DetailView):

    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Usuario
    template_name = 'gestion_usuarios/detalle_usuario.html'
    permission_required = 'gestion_usuarios.detalle_usuario'
    success_url = reverse_lazy('usuarios')


class CrearUsuario(SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Usuario
    form_class = RegistrarUsuarioForm
    template_name = 'gestion_usuarios/registrar_usuario.html'
    permission_required = 'gestion_usuarios.registrar_usuario'
    success_url = reverse_lazy('listado_usuarios')
    success_message = "El Usuario, fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        form = super().form_invalid(form)
        try:
            if form:
                messages.success(self.request, self.success_message)
        except Exception:
            messages.error(self.request, "No se pudo crear el Usuario. Por favor, revise los datos.")
        return form


class ActualizarUsuario(SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Usuario
    form_class = RegistrarUsuarioForm
    template_name= 'gestion_usuarios/registrar_usuario.html'
    permission_required = 'gestion_usuarios.registrar_usuario'
    success_url = reverse_lazy('listado_usuarios')
    success_message = "El Usuario, fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el Usuario. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url


class EliminarUsuario(SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Usuario
    template_name = 'gestion_usuarios/eliminar_usuario.html'
    permission_required = 'gestion_usuarios.eliminar_usuario'
    success_url = reverse_lazy('listado_usuarios')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            identificacion = self.object.identificacion 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"El Usuario con identificacion, {identificacion} fue eliminado exitosamente")
            return result
            
        except Exception:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar el Usuario con identificacion, {identificacion}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)



######-------Crud de los roles-------######

class ListaRoles(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Group
    template_name = 'gestion_roles/listado_roles.html'
    context_object_name = 'roles' 
    permissions = {"any": ('gestion_roles.registrar_rol','gestion_roles.actualizar_rol','gestion_roles.eliminar_rol','gestion_usuarios.registrar_usuario', 'gestion_usuarios.consultar_usuarios', 'gestion_usuarios.actualizar_usuario', 'gestion_usuarios.eliminar_usuario' , 'gestion_usuarios.detalle_usuario' )}



class CrearRol(SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Group
    form_class = RolForm
    template_name = 'gestion_roles/registrar_rol.html'
    permission_required = 'gestion_roles.registrar_rol'
    success_url = reverse_lazy('listado_roles')
    success_message = "El Rol, fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        form = super().form_invalid(form)
        try:
            if form:
                messages.success(self.request, self.success_message)
        except Exception:
            messages.error(self.request, "No se pudo crear el Rol. Por favor, revise los datos.")



class ActualizarRol(SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Group
    form_class = RolForm
    template_name= 'gestion_roles/registrar_rol.html'
    permission_required = 'gestion_roles.registrar_rol'
    success_url = reverse_lazy('listado_roles')
    success_message = "El Rol, fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el Rol. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url


class EliminarRol(SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Group
    template_name = 'gestion_roles/eliminar_rol.html'
    permission_required = 'gestion_roles.eliminar_rol'
    success_url = reverse_lazy('listado_roles')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            identificacion = self.object.identificacion 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"El Rol, {identificacion} fue eliminado exitosamente")
            return result
            
        except Exception:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar el Rol, {identificacion}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista
            return HttpResponseRedirect(self.success_url)