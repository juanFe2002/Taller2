import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Inscripcion
from datetime import datetime



class IncripcionForm(forms.ModelForm): 
    class Meta:
        model = Inscripcion
        fields = ['estudiante','curso','fhecha_inscripcion']
        widgets = {
            'estudiante': forms.TextInput(attrs={'class':'form-control'}),  
            'curso': forms.TextInput(attrs={'class':'form-control'}),  
            'fhecha_inscripcion': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),       
            }
    
    def clean_fhecha_inscripcion(self):
        fhecha_inscripcion = self.cleaned_data.get('fhecha_inscripcion')
        
        if fhecha_inscripcion:
            fecha_actual = datetime.now().date()  # Convertimos a date()
            anio_fecha = fhecha_inscripcion.date() if isinstance(fhecha_inscripcion, datetime) else fhecha_inscripcion  # Convertimos anio a date si es datetime
            
            if anio_fecha < fecha_actual:
                raise ValidationError('La fecha no puede ser mayor a la fecha actual')
        return fhecha_inscripcion




