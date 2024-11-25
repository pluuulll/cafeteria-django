from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'contrasena']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# En forms.py de tu aplicación
from django import forms
from .models import MensajeSoporte

class MensajeSoporteForm(forms.ModelForm):
    class Meta:
        model = MensajeSoporte
        fields = ['nombre', 'email', 'mensaje']
