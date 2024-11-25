from django.db import models
from django import forms

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class LoginForm(forms.Form):
    correo = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput)

class MensajeSoporte(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre}"