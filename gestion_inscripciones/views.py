from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from braces.views import PermissionRequiredMixin, MultiplePermissionsRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


####--------Vistas de la inscripcion--------####
class ListaInscripcion(MultiplePermissionsRequiredMixin, ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Inscripcion
    template_name = 'gestion_inscripciones/listar_inscripciones.html'
    context_object_name = 'inscripciones' 
    permissions = {"any": ('gestion_inscripciones.listar_inscripciones', 'gestion_inscripciones.registrar_inscripcion', 'gestion_inscripciones.actualizar_inscripcion','gestion_inscripciones.eliminar_inscripcion','gestion_inscripciones.detalle_inscricion')}


class CrearInscripcion(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Inscripcion
    form_class = IncripcionForm
    template_name = 'gestion_inscripciones/registrar_inscripcion.html'
    permission_required = 'gestion_inscripciones.registrar_inscripcion'
    success_url = reverse_lazy('listar_inscripciones')
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
        
class ActualizarInscripcion(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Inscripcion
    form_class = IncripcionForm
    template_name= 'gestion_inscripciones/actualizar_inscripcion.html'
    permission_required = 'gestion_inscripciones.actualizar_inscripcion'
    success_url = reverse_lazy('listar_inscripciones')
    success_message = "El Curso fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el Curso. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url
    
    
class EliminarInscripcion(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Cursos
    template_name = 'gestion_inscripciones/eliminar_inscripcion.html'
    permission_required = 'gestion_inscripciones.eliminar_inscripcion'
    success_url = reverse_lazy('listar_inscripciones')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            nombre = self.object.nombre 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"La inscripcion {nombre}, fue eliminado exitosamente")
            return result
            
        except Exception:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar la inscripcion {nombre}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)
