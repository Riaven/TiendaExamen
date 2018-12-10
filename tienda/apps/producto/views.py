from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.producto.forms import ProductoForm
from apps.producto.models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.


# view para el index de la página
def index(request):
    return render (request, 'principal/index.html')


# para poder crear un nuevo producto
def producto_view(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            
            if form.is_valid():
                form.save()
            return redirect('producto:producto_listar')
        else:
            form = ProductoForm()
        return render(request, 'producto/producto_form.html', {'form':form})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')


# para listar todos los productos existentes
def producto_list(request):
    producto = Producto.objects.all()
    contexto = {'productos':producto}
    return render(request, 'producto/producto_list.html', contexto)

#  para poder editar un producto mandando su id
def producto_edit(request, id_producto):

    if request.user.is_superuser:
        producto = Producto.objects.get(id=id_producto)
        if request.method == 'GET':
            form = ProductoForm(instance=producto)
        else:
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
            return redirect('producto_listar')
        return render(request,'producto/producto_form.html',{'form':form})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')


# para poder eliminar un producto mandando su id
def producto_delete(request, id_producto):
    if request.user.is_superuser:    
        producto = Producto.objects.get(id=id_producto)
        if request.method == 'POST':
            producto.delete()
            return redirect('producto_listar')
        return render(request,'producto/producto_delete.html', {'producto':producto})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')
