from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import DatosPersonales, Cargos, Genero, Departamentos


class DatosPersonalesUpdateForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = ['departamentos', 'cargos']



class CrearDatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = ['nombre_completo', 'run', 'direccion', 'telefono', 'fecha_ingreso', 'departamentos', 'cargos', 'genero']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese un nombre de Usuario'}),
            'run': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese el Run'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese la Direccion'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese el Fono'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date', 'placeholder': 'Ingrese fecha de ingreso'}),
            'departamentos': forms.Select(attrs={'class': 'form-control form-select'}),
            'cargos': forms.Select(attrs={'class': 'form-control form-select'}),
            'genero': forms.Select(attrs={'class': 'form-control form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(CrearDatosPersonalesForm, self).__init__(*args, **kwargs)

        # Esto es para agregar la opción "Seleccionar Cargo" al principio
        cargos_choices = [(None, 'Seleccionar Cargo')] + [(cargo.id_cargo, cargo.nombre_cargo) for cargo in Cargos.objects.all()]
        self.fields['cargos'].widget.choices = cargos_choices

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre de Usuario'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Contraseña'}),
        }

            
# Register
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese un nombre de Usuario'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese su Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese su Contraseña'}),
        }

