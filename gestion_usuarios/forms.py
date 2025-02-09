from .models import *
from django import forms
from django.contrib.auth.models   import Group
from django.db.models import Case, When
from .listado_permisos import LISTADO_PERMISOS

class RegistrarUsuarioForm(forms.ModelForm):
    def __init__ (self, *args, **kwargs):
        super(RegistrarUsuarioForm, self).__init__(*args, **kwargs)
        self.instancia = kwargs.get('instance', None)
        orden_permisos = Case(*[When(codename=codename, then=pos) for pos, codename in enumerate(LISTADO_PERMISOS)])
        self.fields['user_permissions'].label = "Permisos Adicionales del Usuario"
        self.fields["user_permissions"].queryset = self.fields["user_permissions"].queryset.filter(codename__in=LISTADO_PERMISOS)\
            .order_by(orden_permisos)
        self.fields["groups"].required = True
        self.fields["groups"].label = "Rol de usuario"
            
    class Meta:
        model = Usuario
        fields = ('tipo_identificacion', 'identificacion', 
                'first_name', 'last_name',
                'email','genero', 'ciudad', 
                'telefono','groups', 'user_permissions' )
        widgets = {
            'tipo_identificacion': forms.Select(attrs={ 'width': "60%", 'col': "4", 'class':'form-control'}),
            'identificacion': forms.TextInput(attrs={'width': "60%", 'col': "4",'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'width': "60%", 'col': "4",'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'width': "60%", 'col': "4",'class':'form-control'}),
            'email': forms.EmailInput(attrs={'width': "60%", 'col': "4",'class':'form-control'}),
            'genero': forms.Select(attrs={'width': "60%", 'col': "4",'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'width': "60%", 'col': "4",'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'width': "60%", 'col': "4",'class':'form-control'}),
            'groups': forms.SelectMultiple(attrs={'width': "60%", 'col': "4",'class':'form-control'}),
            'user_permissions': forms.SelectMultiple(attrs={'width': "60%", 'col': "4",'class':'form-control'}),
        }
        
        def clean_email(self):
            email = self.clean_data['email']
            if not self.instance is None:
                pk_usuario = self.instance.pk
                usuario = Usuario.objects.get(id=pk_usuario)
                usuarios = Usuario.objects.filter(email=email, username=email)
                if usuarios.exists():
                    if not usuario in usuarios:
                        self.errors["email"] = ["El correo electronico ya se encuentra registrado en el sistmea"]
            else:
                if Usuario.objects.filter(email=email, username=email).exists():
                    self._errors["email"] = ["El correo electrónico ya se encuentra registrado en el sistema."]
            return email.lower()
        
class LoginForm(forms.Form):
    username = forms.CharField(label="Correo Electronico", max_length=80, widget= forms.TextInput(attrs={
        'id': 'usernameInput', 'placeholder': 'Correo Electronico', 'class': 'form-control'}))
    
    password = forms.CharField(label="Contraseña", max_length=50, widget=forms.TextInput(attrs={
        'type': 'password', 'id': 'passwordInput', 'placeholder': 'Contraseña', 'class': 'form-control'}))
    
    
class RolForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("name", "permissions",)
        widgets = {
            'permissions': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
    
    @staticmethod
    def label_from_instance(self, obj):
        return "%s" % obj.name
    
    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nombre del Rol"
        orden_permisos = Case(*[When(codename=codename, then=pos) for pos, codename in enumerate(LISTADO_PERMISOS)])
        self.fields["permissions"].queryset =self.fields["permissions"].queryset.filter(codename__in=LISTADO_PERMISOS)\
            .order_by(orden_permisos) 
        self.fields["permissions"].label = "Permisos Asignados al Rol"