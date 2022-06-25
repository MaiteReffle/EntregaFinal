from django.db import models

class Sucursales(models.Model):
    nombreSucursal=models.CharField(max_length=40)
    direccionSucursal=models.CharField(max_length=40)
    idSucursal=models.IntegerField(primary_key=True)
    fechaDeInauguracionSucursal=models.DateField()

    def __str__(self):
        return str(self.idSucursal)+" "+str(self.nombreSucursal)

class Clases(models.Model):
    idClase=models.IntegerField(primary_key=True)
    nombreClase=models.CharField(max_length=40)
    sucursalClase = models.CharField(max_length=40)
    profesorClase = models.CharField(max_length=40)

    def __str__(self):
        return str(self.nombreClase)

class Profesores(models.Model):
    id=models.IntegerField(primary_key=True)
    nombreProfesor=models.CharField(max_length=40)
    apellidoProfesor=models.CharField(max_length=40)
    nombreClaseProfesor=models.CharField(max_length=60)
    fechaDeNacimientoProfesor=models.DateField()

    def __str__(self):
        return str(self.id)+" "+self.nombreProfesor+" "+str(self.apellidoProfesor)

class Horarios(models.Model):
    idHorario=models.IntegerField(primary_key=True)
    nombreClaseH=models.CharField(max_length=40)
    horarioClase=models.TimeField()

    def __str__(self):
        return str(self.idHorario)+" "+str(self.nombreClaseH)+" "+str(self.horarioClase)