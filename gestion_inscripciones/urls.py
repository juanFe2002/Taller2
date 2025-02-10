from django.urls import path
from .views import *

urlpatterns = [
    ####--------Incripcion--------####
    path("listar_inscripciones", ListaInscripcion.as_view(), name='listar_inscripciones'),
    path("registrar_inscripcion", CrearInscripcion.as_view(), name='registrar_inscripcion'),
    path("actualizar_inscripcion/<int:pk>/", ActualizarInscripcion.as_view(), name='actualizar_inscripcion'),
    path("eliminar_inscripcion/<int:pk>/", EliminarInscripcion.as_view(), name='eliminar_inscripcion'),   
]