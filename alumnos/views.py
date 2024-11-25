from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm  # Importar LoginForm
from .models import MensajeSoporte  # Asegúrate de usar el nombre correcto del modelo aquí
from django.http import HttpResponseRedirect
from .forms import LoginForm
from .forms import MensajeSoporteForm 


def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def login_view(request):
    return render(request, 'login.html')

def info(request):
    return render(request, 'info.html')

def carrito(request):
    return render(request, 'carrito.html')

def comentarios(request):
    return render(request, 'comentarios.html')

def alo(request):
    return render(request, 'alo.html')

def perfil(request):
    return render(request, 'perfil.html')

def soporte(request):
    return render(request, 'soporte.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = UsuarioForm()
    return render(request, 'registrar_usuario.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html')  # cambiar 'index' por la URL a tu página principal
            else:
                messages.error(request, 'Email o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # redirige de vuelta al login después de cerrar sesión

def home(request):
    return render(request, 'home.html')

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')

def soporte(request):
    if request.method == 'POST':
        form = MensajeSoporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soporte_exitoso')  # Redirigir a una página de éxito
    else:
        form = MensajeSoporteForm()
    
    return render(request, 'soporte.html', {'form': form})