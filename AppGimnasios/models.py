from django.db import models

class Sucursales(models.Model):
    nombreSucursal=models.CharField(max_length=40)
    direccionSucursal=models.CharField(max_length=40)
    idSucursal=models.IntegerField(primary_key=True)
    fechaDeInauguracionSucursal=models.DateField()

    def __str__(self):
        return self.nombreSucursal+" "+str(self.idSucursal)

class Clases(models.Model):
    idClase=models.IntegerField(primary_key=True)
    nombreClase=models.CharField(max_length=40)

    def __str__(self):
        return self.nombreClase+" "+str(self.idClase)

class Profesores(models.Model):
    nombreProfesor=models.CharField(max_length=40)
    apellidoProfesor=models.CharField(max_length=40)
    nombreClaseProfesor=models.CharField(max_length=60)
    fechaDeNacimientoProfesor=models.DateField()

    def __str__(self):
        return self.nombreProfesor+""+str(self.nombreProfesor)

class Horarios(models.Model):
    idHorario=models.IntegerField(primary_key=True)
    nombreClaseH=models.CharField(max_length=40)
    horarioClase=models.TimeField()

    def __str__(self):
        return self.nombreClaseH+" "+str(self.idHorario)