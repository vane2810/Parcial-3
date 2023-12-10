from django import forms

class Add_proveedor(forms.Form):
    nombre = forms.CharField(max_length=100)
    marca = forms.CharField(max_length=100)
    contacto = forms.CharField(max_length=20)