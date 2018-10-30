from django import forms
from .models import Rescatado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

class RescatadoForm(forms.ModelForm):
    

    class Meta:
        model = Rescatado
        fields = ('fotografia', 'nombre', 'raza', 'descripcion', 'estado',)
    
class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=False, help_text='Opcional.')
    apellido = forms.CharField(max_length=30, required=False, help_text='Opcional.')
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo válida.')
    password1 = forms.CharField(label=_("Contraseña"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Confirme Contraseña"),
        widget=forms.PasswordInput,
        help_text=_("Ingrese la misma contraseña, para su verificación."))

    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido', 'email', 'password1', 'password2', )