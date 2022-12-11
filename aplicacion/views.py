from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from .forms import InputForm

from .models import Proyecto


# Create your views here.
def inicio(request):
    Listado = Proyecto.objects.all()
    return render(request, 'index.html', {'Listado':Listado})


from django.contrib.auth import logout
def salir(request):
    auth.logout(request)
    Listado = Proyecto.objects.all()
    return render(request, 'index.html', {'Listado': Listado})



@login_required(login_url='logeador')
def proyectos(request):
    formulario = InputForm

    if request.method == 'POST':
        create_form = InputForm(request.POST)

        if create_form.is_valid():
            titulo = request.POST.get('Titulo')
            descripcion = request.POST.get('Descripción')
            tags = request.POST.get('Tags')
            imagen = request.POST.get('Foto')
            url_github = request.POST.get('URL_GIT')

            proyecto = Proyecto(foto=imagen,
                                titulo=titulo,
                                descripcion=descripcion,
                                tags=tags,
                                url_github=url_github)
            proyecto.save()
            messages.success(request, 'El proyecto se creo correctamente')
            return redirect('proyectos')
        else:
            messages.warning(request, create_form.errors)
            return redirect('proyectos')
    else:
        return render(request, 'proyectos.html', {'forms': formulario})


def logeador(request):

    if request.method == 'POST':
            usuario = request.POST['Husuario']
            contra = request.POST['Hcontra']
            user = auth.authenticate(username=usuario, password=contra)

            if user is not None:
                auth.login(request, user)
                #mensaje para consola si usuario logeado
                print("Consola SE LOGEO")
                return redirect('proyectos')
            else:
                messages.success(request, 'ERROR NO ESTAS REGISTRADO')
                return redirect('logeador')
    else:
        return render(request, 'login.html')


def registrar(request):
    # Si el motodo es POST
    if request.method == 'POST':
        usuario = request.POST['Husuario']
        correo = request.POST['Hcorreo']
        nombre = request.POST["Hnombres"]
        apellido = request.POST["Hapellidos"]
        contra = request.POST['Hcontra']
        contras = request.POST['Hcontras']

        # Si las contraseñas son iguales entonces guardamos en la tabla User
        if contra == contras:
            user = User.objects.create_user(
                username=usuario,
                first_name=nombre,
                last_name=apellido,
                email=correo, password=contra)
            user.save()
            return redirect('logeador')
        else:
            messages.success(request, 'Una contraseña no Coincide')
            return redirect('registrar')

    return render(request, 'registrar.html')
