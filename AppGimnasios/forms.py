from django import forms

class SucursalesFormulario(forms.Form):
    nombreSucursal=forms.CharField(max_length=40)
    direccionSucursal=forms.CharField(max_length=40)
    fechaDeInauguracionSucursal=forms.DateField()

class ClasesFormulario(forms.Form):
    nombreClase=forms.CharField(max_length=40)

class ProfesoresFormulario(forms.Form):
    nombreProfesor=forms.CharField(max_length=40)
    apellidoProfesor=forms.CharField(max_length=40)
    nombreClaseProfesor=forms.CharField(max_length=60)
    fechaDeNacimientoProfesor=forms.DateField()

class HorariosFormulario(forms.Form):
    nombreClaseH=forms.CharField(max_length=40)
    horarioClase=forms.TimeField()