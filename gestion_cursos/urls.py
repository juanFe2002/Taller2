from django.urls import path
from .views import *

urlpatterns = [
    ####--------Curso--------####
    path("listar_cursos", ListaCurso.as_view(), name='listar_cursos'),
    path("registrar_curso", CrearCurso.as_view(), name='registrar_curso'),
    path("actualizar_curso/<int:pk>/", ActualizarCurso.as_view(), name='actualizar_curso'),
    path("eliminar_curso/<int:pk>/", EliminarCurso.as_view(), name='eliminar_curso'),   
    
    ####--------Materias--------####
    path("listar_materias", ListaMateria.as_view(), name='listar_materias'),
    path("registrar_materia", CrearMateria.as_view(), name='registrar_materia'),
    path("actualizar_materia/<int:pk>/", ActualizarMateria.as_view(), name='actualizar_materia'),
    path("vista_matria/<int:pk>/", VistaMateria.as_view(), name='vista_matria'),
    path("eliminar_materia/<int:pk>/", EliminarMateria.as_view(), name='eliminar_materia'),
]