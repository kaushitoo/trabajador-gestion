from django.db import models

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=30)

    def __str__(self):
        return self.sexo

class Parentesco(models.Model):
    id_parentesco = models.AutoField(primary_key=True)
    parentesco = models.CharField(max_length=40)

    def __str__(self):
        return self.parentesco

class Cargos(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_cargo

class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_departamento

class DatosPersonales(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    run = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12, unique=True)
    fecha_ingreso = models.DateTimeField()
    departamentos = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    cargos = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo

class CargasFamiliares(models.Model):
    id_cargas = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    run = models.CharField(max_length=10, unique=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE)
    usuarios = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo

class ContactosEmergencia(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=12, unique=True)
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE)
    usuarios = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo
