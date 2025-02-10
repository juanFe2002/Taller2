from django.db import models
from gestion_usuarios.models import *
from gestion_cursos.models import *

class Inscripcion(models.Model):
    """Clase modelo Inscripcion para el registro de datos de una Inscripcion.
    
    :param models: Administrar datos de una Inscripcion en curso
    :type models: Objeto
    :return: Una instancia de la clase Inscripcion con los datos registrados
    :rtype: Objeto
    """
    estudiante = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name = 'Estudiante*')
    curso = models.ForeignKey(Cursos, on_delete=models.PROTECT, verbose_name = 'Cursos por elegir*') 
    fhecha_inscripcion = models.DateField(verbose_name = 'Fecha incripcion*') 
    class Meta:
        
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('registrar_inscripcion', 'Puede Crear inscripcion'),
            ('listar_inscripciones', 'Puede Consultar inscripciones'),
            ('actualizar_inscripcion', 'Puede Actualizar inscripcion'),
            ('eliminar_inscripcion', 'Puede Eliminar inscripcion'),  
        )
    
    def __str__(self):
        return  str(self.curso) + '-' + str(self.fhecha_inscripcion)
    
    @staticmethod
    def listar_inscripciones():
        return Inscripcion.objects.all()