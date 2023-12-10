from django import forms
from app.models import Articulos

class Add_cliente(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    contacto = forms.CharField(max_length=20)
    articuloID = forms.ModelChoiceField(queryset=Articulos.objects.all())
