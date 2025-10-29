from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from main.models import Usuario

def index(request):
    return render(request, 'main/index.html')

def registro_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if Usuario.objects.filter(ema_usu=email).exists():
            messages.warning(request, "El correo ya está registrado.")
        else:
            hashed_password = make_password(password)

            Usuario.objects.create(
                nom_usu=nombre,
                ape_usu=apellido,
                ema_usu=email,
                con_usu=hashed_password,
                id_rol_id=13 
            )
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('login')

    return render(request, "main/registro.html")

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            usuario = Usuario.objects.get(ema_usu=email)
            if check_password(password, usuario.con_usu):
                request.session['usuario_id'] = usuario.id_usu
                request.session['usuario_nombre'] = usuario.nom_usu
                request.session['rol'] = usuario.id_rol_id

                messages.success(request, f"Bienvenido {usuario.nom_usu}")

                rol = usuario.id_rol.nom_rol.lower()
                if rol == "administrador":
                    return redirect('panel_admin')
                elif rol == "estudiante":
                    return redirect('panel_estudiante')
                elif rol == "acudiente":
                    return redirect('panel_acudiente')
                elif rol == "administrativo":
                    return redirect('panel_administrativo')
                else:
                    messages.warning(request, "Rol desconocido.")
                    return redirect('login')
            else:
                messages.error(request, "Contraseña incorrecta.")
                return redirect('login')

        except Usuario.DoesNotExist:
            messages.error(request, "Correo no registrado.")
            return redirect('login')

    return render(request, 'main/login.html')


def panel_admin(request):
    return render(request, 'main/admin_panel/panel_admin.html')

def panel_estudiante(request):
    return render(request, 'main/estudiante_panel/panel_estudiante.html')

def panel_acudiente(request):
    return render(request, 'main/acudiente_panel/panel_acudiente.html')

def panel_administrativo(request):
    return render(request, 'main/administrativo_panel/panel_administrativo.html')
