from django.contrib import admin
from .models import Proveedores, Articulos, Clientes

# Registro de modelos
admin.site.register(Proveedores)
admin.site.register(Articulos)
admin.site.register(Clientes)