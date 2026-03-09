from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'fecha_nacimiento',
            'identificacion',
            'telefono',
            'direccion',
            'sexo'
        ]

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }