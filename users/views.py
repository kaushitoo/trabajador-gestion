from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, DatosPersonalesUpdateForm, CrearDatosPersonalesForm, UserLoginForm

@login_required
def eliminar_trabajador(request, id):
    trabajador = get_object_or_404(DatosPersonales, id_usuario=id)

    if request.method == 'POST':
        trabajador.delete()
        return redirect('listaTrabajadores')

    return render(request, 'jefe/eliminar_trabajador.html', {'trabajador': trabajador})


@login_required
def actualizar_trabajador(request, id):
    trabajador = get_object_or_404(DatosPersonales, id_usuario=id)

    if request.method == 'POST':
        form = DatosPersonalesUpdateForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('listaTrabajadores')
    else:
        form = DatosPersonalesUpdateForm(instance=trabajador)

    return render(request, 'jefe/actualizar_trabajador.html', {'form': form})




def signin(request):
    error = None

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                error = "Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo."
    else:
        form = UserLoginForm()

    return render(request, 'signin.html', {'form': form, 'error': error})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {"form": SignUpForm(), "error": "Username or email already exists."})
        else:
            return render(request, 'signup.html', {"form": form, "error": "Error in the form."})
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {"form": form})

def home(request):
    return render(request, 'home.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')




def inicioJefe(request):
    return render(request, 'jefe/inicio.html')




from .models import DatosPersonales

def listaTrabajadores(request):
    trabajadores = DatosPersonales.objects.all()
    return render(request, 'jefe/listaTrabajadores.html', {'trabajadores': trabajadores})



def datoslaborales(request):
    return render (request, 'jefe/datoslaborales.html')







def inicioPersonal(request):
    return render(request, 'personal/inicio.html')


def listaTrabajadoresP(request):
    trabajadores = DatosPersonales.objects.all()
    return render(request, 'personal/listaTrabajadores.html', {'trabajadores': trabajadores})



@login_required
def crear_trabajador(request):
    if request.method == 'POST':
        form = CrearDatosPersonalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaTrabajadoresP')
    else:
        form = CrearDatosPersonalesForm()

    return render(request, 'personal/crear_trabajador.html', {'form': form})


@login_required
def actualizar_trabajadorP(request, id):
    trabajador = get_object_or_404(DatosPersonales, id_usuario=id)

    if request.method == 'POST':
        form = DatosPersonalesUpdateForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('listaTrabajadoresP')
    else:
        form = DatosPersonalesUpdateForm(instance=trabajador)

    return render(request, 'personal/actualizar_trabajador.html', {'form': form})

