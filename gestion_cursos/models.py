from django.db import models
from gestion_usuarios.models import *

class Cursos(models.Model):
    """Clase modelo Cursos para el registro de datos de un Curso.
    
    :param models: Administrar datos de un Curso en curso
    :type models: Objeto
    :return: Una instancia de la clase Cursos con los datos registrados
    :rtype: Objeto
    """
    
    nombre = models.CharField(max_length=50, verbose_name = 'Nombre del curso*', unique=True) 
    
    class Meta:
        
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('registrar_curso', 'Puede Crear Curso'),
            ('listar_cursos', 'Puede Consultar Cursos'),
            ('actualizar_curso', 'Puede Actualizar Curso'),
            ('eliminar_curso', 'Puede Eliminar Curso'),  
        )
    
    def __str__(self):
        return  str(self.nombre)



class Materias(models.Model):
    """Clase modelo Materias para el registro de datos de un Materia.
    
    :param models: Administrar datos de una Materia
    :type models: Objeto
    :return: Una instancia de la clase Materias con los datos registrados
    :rtype: Objeto
    """
    
    materia = models.CharField(max_length=50, verbose_name = 'Materia*', unique=True) 
    nombre_curso = models.ForeignKey(Cursos, on_delete=models.PROTECT, verbose_name = 'Curso*')
    maestro = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name = 'Maestro asignado*')
    
    
    class Meta:
        
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('registrar_materia', 'Puede Crear Materia'),
            ('listar_materias', 'Puede Consultar Materias'),
            ('actualizar_materia', 'Puede Actualizar Materia'),
            ('eliminar_materia', 'Puede Eliminar Materia'),
            ('detalle_materia', 'Puede Ver Detalle Materia'),  
        )
    
    def __str__(self):
        return  str(self.materia) + ' - ' + str(self.nombre_curso.nombre) + ' - ' + str(self.maestro)
    
    @staticmethod
    def listar_materias():
        return Materias.objects.all()