from django import forms
from .models import Rescatado

class RescatadoForm(forms.ModelForm):
    

    class Meta:
        model = Rescatado
        fields = ('fotografia', 'nombre', 'raza', 'descripcion', 'estado',)