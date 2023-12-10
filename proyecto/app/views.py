from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .formularios.registerform import NewUserForm
from .formularios.loginform import LoginForm
from .formularios.add_clientes import Add_cliente
from .formularios.add_proveedores import Add_proveedor
from .formularios.add_articulos import Add_articulo
from .models import Proveedores, Articulos, Clientes    

#Vista de inicio
def home(request):
    return render(request, 'home.html')

# Vista para registrar usuarios
def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect('/')
    else:
        formulario = NewUserForm()
        return render(request, "Reg_user.html", {"form": formulario})

#Vista de la pagina principal despues de iniciar sesion
@login_required(login_url='login')
def index(request):
    es_cliente = request.user.groups.filter(name='Cliente').exists()
    es_gerente = request.user.groups.filter(name='Gerente').exists()
    return render(request, 'index.html', {'user': request.user, 'es_gerente': es_gerente, 
'es_cliente': es_cliente})

# Vista para iniciar sesion
def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'fom': form})

# Cerrar sesion
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

#Vista para la lista de articulos
@login_required(login_url='login')
def list_articulo(request):
    es_cliente = request.user.groups.filter(name='Cliente').exists()
    es_gerente = request.user.groups.filter(name='Gerente').exists()
    articulos = Articulos.objects.all()
    return render(request, "lis_articulos.html", {'artic': articulos, 'user': request.user, 'es_gerente': es_gerente, 'es_cliente': es_cliente})

# Vista para la lista de proveedores
@login_required(login_url='login')
def list_proveedor(request):
    proveedor = Proveedores.objects.all()
    return render(request, "lis_proveedor.html", {'prov': proveedor})

# Vista para la lista de clientes
@login_required(login_url='login')
def list_cliente(request):
    clientes = Clientes.objects.all()
    return render(request, "lis_cliente.html", {'cl': clientes })

# Vista para añadir clientes
@login_required(login_url='login')
def cliente_add(request):
    if request.method == "POST":
        formulario = Add_cliente(request.POST)
        if formulario.is_valid():
            nuevoreg = Clientes()
            nuevoreg.nombre = formulario.cleaned_data["nombre"]
            nuevoreg.apellido = formulario.cleaned_data["apellido"]
            nuevoreg.contacto = formulario.cleaned_data["contacto"]
            nuevoreg.articuloID = formulario.cleaned_data["articuloID"]
            nuevoreg.save()
            return HttpResponseRedirect("/clientes/")
    else:
        formulario = Add_cliente()
        return render(request, "Add_clientes.html", {"ad_cli": formulario})

# Lista para añadir proveedores
@login_required(login_url='login')
def proveedor_add(request):
    if request.method == "POST":
        formulario = Add_proveedor(request.POST)
        if formulario.is_valid():
            nuevoreg = Proveedores()
            nuevoreg.nombre = formulario.cleaned_data["nombre"]
            nuevoreg.marca = formulario.cleaned_data["marca"]
            nuevoreg.contacto = formulario.cleaned_data["contacto"]
            nuevoreg.save()
            return HttpResponseRedirect("/proveedores/")
    else:
        formulario = Add_proveedor()
        return render(request, "Add_proveedores.html", {"ad_pro": formulario})

# Vista pa ra añadir articulos
@login_required(login_url='login')
def articulo_add(request):
    if request.method == "POST":
        formulario = Add_articulo(request.POST)
        if formulario.is_valid():
            nuevoreg = Articulos()
            nuevoreg.nombre = formulario.cleaned_data["nombre"]
            nuevoreg.precio = formulario.cleaned_data["precio"]
            nuevoreg.descripcion= formulario.cleaned_data["descripcion"]
            nuevoreg.proveedorID = formulario.cleaned_data["proveedorID"]
            nuevoreg.save()
            return HttpResponseRedirect("/articulos/")
    else:
        formulario = Add_articulo()
        return render(request, "Add_articulos.html", {"ad_art": formulario})