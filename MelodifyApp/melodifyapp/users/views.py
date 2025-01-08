from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserCreationForm
from .models import User
from .decorators import user_type_required


# Vista de inicio
def inicio(request):
    """Página de inicio."""
    return render(request, 'home.html')


# Vista de registro de usuario
def register_view(request):
    """Registra a un nuevo usuario."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Crea el usuario
            messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
            return redirect('users:login')  # Redirigir al login después del registro
        else:
            messages.error(request, "Hubo un error en el formulario. Por favor verifica tus datos.")
    else:
        form = UserCreationForm()  # Crear una instancia vacía del formulario
    return render(request, 'register.html', {'form': form})


# Vista de inicio de sesión
def login_view(request):
    """Autentica al usuario y redirige al dashboard correspondiente."""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            # Redirige directamente al dashboard según el rol del usuario
            return redirect('users:redirect_dashboard')
        else:
            messages.error(request, "Credenciales incorrectas. Inténtalo nuevamente.")
    return render(request, 'login.html')


# Vista para cerrar sesión
def logout_view(request):
    """Cierra sesión y redirige al login."""
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('users:login')


# Redirige al dashboard correspondiente según el tipo de usuario
@login_required
def redirect_dashboard(request):
    """Redirige al dashboard según el tipo de usuario."""
    role_dashboard = {
        'M': 'users:musico_dashboard',
        'O': 'users:oyente_dashboard',
        'P': 'users:productor_dashboard',
    }
    user_role = request.user.user_type
    dashboard_url = role_dashboard.get(user_role)
    if dashboard_url:
        return redirect(dashboard_url)
    else:
        messages.error(request, "Tu rol no está definido correctamente.")
        return redirect('users:login')  # Redirigir al login si no tiene rol definido


# Dashboard de músico
@login_required
@user_type_required('M')  # Decorador para verificar el tipo de usuario
def musico_dashboard(request):
    """Dashboard para músicos."""
    return render(request, 'musico_dashboard.html')


# Dashboard de oyente
@login_required
@user_type_required('O')  # Decorador para verificar el tipo de usuario
def oyente_dashboard(request):
    """Dashboard para oyentes."""
    return render(request, 'oyente_dashboard.html')


# Dashboard de productor
@login_required
@user_type_required('P')  # Decorador para verificar el tipo de usuario
def productor_dashboard(request):
    """Dashboard para productores."""
    return render(request, 'productor_dashboard.html')
