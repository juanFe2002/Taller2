import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Materias
from .models import Cursos



class CursosForm(forms.ModelForm): 
    class Meta:
        model = Cursos
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),       
            }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if self.instance.pk:  # Si estamos editando
            if Cursos.objects.filter(nombre=nombre).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un Curso en el registro de cursos')
        else:  # Si estamos creando
            if Cursos.objects.filter(nombre=nombre).exists():
                raise ValidationError('Ya existe un Curso en el registro de cursos')
        
        return nombre

class MateriasForm(forms.ModelForm): 
    class Meta:
        model = Materias
        fields = ['materia','nombre_curso','maestro']
        widgets = {
            'materia': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_curso':forms.Select(attrs={'class':'form-control'}),
            'maestro': forms.Select(attrs={'class':'form-control'}),        
            }
    
    def clean_materia(self):
        materia = self.cleaned_data.get('materia')
        if self.instance.pk:  # Si estamos editando
            if Materias.objects.filter(materia=materia).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe una Materia en el registro ')
        else:  # Si estamos creando
            if Materias.objects.filter(materia=materia).exists():
                raise ValidationError('Ya existe una Materia en el registro')
        
        return materia




