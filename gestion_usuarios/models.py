from django.db import models
from django.contrib.auth.models import Permission, AbstractUser



class Usuario(AbstractUser):
    
    """Creación de usuarios """
    TIPOS_ID = (
        ("CC", "Cédula de ciudadanía"),
        ("TI", "Tarjeta de identidad"),
        ("RC", "Registro civil"),
        ("CE", "Cédula de extranjería"),
        ("PPN", "Pasaporte"),
        ("SSN", "Seguridad social"),
        ("DNI", "Documento nacional de identidad"),
        ("LIC", "Licencia"),
    )
    GENERO = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    )
    
    tipo_identificacion = models.CharField(max_length=10, choices=TIPOS_ID, verbose_name='Tipo Identificación')
    identificacion = models.CharField(max_length=100, verbose_name='No. Identificación', unique=True)
    telefono = models.CharField(max_length=10, verbose_name='Teléfono') 
    ciudad = models.CharField(max_length=200, verbose_name='Ciudad')
    genero = models.CharField(max_length=50, choices=GENERO, verbose_name="Genero")
    
    class Meta:
        ordering = ['-first_name']
        default_permissions = ()
        permissions = (
            ('registrar_usuario', 'Puede Registrar Usuario'),
            ('listar_usuarios', 'Puede Consultar Usuarios'),
            ('actualizar_usuario', 'Puede Actualizar Usuario'),
            ('eliminar_usuario', 'Puede Eliminar Usuario'),
            ('detalle_usuario', 'Puede Ver Detalle Usuario'), 
        )
        
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        if not self.pk:
            self.set_password(self.first_name + self.last_name + '-' + str(self.identificacion))
        super(Usuario, self).save(*args, **kwargs)
    
    
class Roles(models.Model):
    class Meta:
        managed = False
        default_permissions = ()
        permissions = (
            ('registrar_rol', 'Puede Registrar Rol'),
            ('listar_roles', 'Puede Consultar Roles'),
            ('actualizar_rol', 'Puede Actualizar Rol'),
            ('eliminar_rol', 'Puede eliminar Rol'),
        )
