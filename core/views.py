from django.shortcuts import render,redirect
from core.forms import ProductoForm
from .models import Producto

#class Producto:
#   def __init__(self, nombre, valor):
#        self.nombre = nombre
#        self.valor = valor
#        super().__init__()

# Create your views here.
#def home(request):

#    arroz = Producto("Diana", 2500)

#    familiares = ["Tio", "Primo", "Prima"]
#    contexto = {"nombre": "Jhon Suaza", "familia": familiares, "arroz": arroz}

#    return render(request, "core/home.html", contexto)

def home(request):
    productos = Producto.objects.all()
    contexto = {
        "productos": productos
    }
    return render(request, "core/home.html", contexto)

def form_producto(request):
    formulario = ProductoForm()

    contexto = {
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request, "core/form_productos.html", contexto)

def form_mod_producto(request,id):
    producto = Producto.objects.get(idProducto = id)

    contexto = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Actualizado Correctamente"
    return render(request, "core/form_mod_producto.html", contexto)
    
def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto = id)
    producto.delete()
    return redirect (to="home")