from django.contrib import admin
from .models import Genero, Parentesco, Cargos, Departamentos, DatosPersonales, CargasFamiliares, ContactosEmergencia

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display =['sexo']

@admin.register(Parentesco)
class ParentescoAdmin(admin.ModelAdmin):
    list_display = ['parentesco']

@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    list_display = ['nombre_cargo']

@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ['nombre_departamento']

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display =['nombre_completo', 'run', 'direccion', 'telefono', 'fecha_ingreso', 'departamentos', 'cargos', 'genero']

@admin.register(CargasFamiliares)
class CargasFamiliaresAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'run', 'genero', 'parentesco', 'usuarios']

@admin.register(ContactosEmergencia)
class ContactosEmergenciaAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'telefono', 'parentesco', 'usuarios']
