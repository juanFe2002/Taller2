from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from braces.views import PermissionRequiredMixin, MultiplePermissionsRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


####--------Vistas del curso--------####
class ListaCurso(MultiplePermissionsRequiredMixin, ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Cursos
    template_name = 'gestion_cursos/listar_cursos.html'
    context_object_name = 'cursos' 
    permissions = {"any": ('gestion_cursos.listar_cursos', 'gestion_cursos.registrar_curso', 'gestion_cursos.actualizar_curso', 'gestion_cursos.eliminar_curso')}


class CrearCurso(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Cursos
    form_class = CursosForm
    template_name = 'gestion_cursos/registrar_curso.html'
    permission_required = 'gestion_cursos.registrar_curso'
    success_url = reverse_lazy('listar_cursos')
    success_message = "El Curso fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        form = super().form_invalid(form)
        try:
            if form:
                messages.success(self.request, self.success_message)
        except Exception:
            messages.error(self.request, "No se pudo crear el Curso. Por favor, revise los datos.")
        return form
        
class ActualizarCurso(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Cursos
    form_class = CursosForm
    template_name= 'gestion_cursos/actualizar_curso.html'
    permission_required = 'gestion_cursos.actualizar_curso'
    success_url = reverse_lazy('listar_cursos')
    success_message = "El Curso fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el Curso. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url
    
    
class EliminarCurso(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Cursos
    template_name = 'gestion_cursos/eliminar_curso.html'
    permission_required = 'gestion_cursos.eliminar_curso'
    success_url = reverse_lazy('listar_cursos')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            nombre = self.object.nombre 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"El Curso {nombre}, fue eliminado exitosamente")
            return result
            
        except Exception:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar el Curso {nombre}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)


####--------Vistas de la materia--------####
class ListaMateria(MultiplePermissionsRequiredMixin, ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Materias
    template_name = 'gestion_materias/listar_materias.html'
    context_object_name = 'materias' 
    permissions = {"any": ('gestion_materias.listar_materias', 'gestion_materias.registrar_materia', 'gestion_materias.actualizar_materia','gestion_materias.detalle_materia','gestion_materias.eliminar_materia')}


class VistaMateria(PermissionRequiredMixin, DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Materias
    template_name = 'gestion_materias/vista_materia.html'
    permission_required = 'gestion_materias.vista_materia'
    success_url = reverse_lazy('materias')



class CrearMateria(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Materias
    form_class = MateriasForm
    template_name = 'gestion_materias/registrar_materia.html'
    permission_required = 'gestion_materias.registrar_materia'
    success_url = reverse_lazy('listar_materias')
    success_message = "La Materia fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        form = super().form_invalid(form)
        try:
            if form:
                messages.success(self.request, self.success_message)
        except Exception:
            messages.error(self.request, "No se pudo crear la Materia. Por favor, revise los datos.")
        return form
        
class ActualizarMateria(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Materias
    form_class = MateriasForm
    template_name= 'gestion_materias/actualizar_materia.html'
    permission_required = 'gestion_materias.actualizar_materia'
    success_url = reverse_lazy('listar_materias')
    success_message = "La Materia fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar la Materia. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url
    
    
class EliminarMateria(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Materias
    template_name = 'actualizar_materia/eliminar_materia.html'
    permission_required = 'actualizar_materia.eliminar_materia'
    success_url = reverse_lazy('listar_cursos')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            nombre = self.object.nombre 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"La Materia {nombre}, fue eliminado exitosamente")
            return result
            
        except Exception:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar la Materia {nombre}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)