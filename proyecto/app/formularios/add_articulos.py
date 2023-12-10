from django import forms
from app.models import Proveedores

class Add_articulo(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.FloatField()
    descripcion = forms.CharField(max_length=255)
    proveedorID = forms.ModelChoiceField(queryset=Proveedores.objects.all())
