from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.sucursal.forms import SucursalForm
from apps.sucursal.models import Sucursal
from django.contrib.auth.decorators import login_required


# Create your views here.


# para poder crear una nueva sucursal
def sucursal_view(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = SucursalForm(request.POST)
            
            if form.is_valid():
                form.save()
            return redirect('sucursal:sucursal_listar')
        else:
            form = SucursalForm()
        return render(request, 'sucursal/sucursal_form.html', {'form':form})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')


# para listar todos las sucursales existentes
def sucursal_list(request):
    sucursal = Sucursal.objects.all()
    contexto = {'sucursales':sucursal}
    return render(request, 'sucursal\sucursal_list.html', contexto)

#  para poder editar una sucursal mandando su id
def sucursal_edit(request, id_sucursal):

    if request.user.is_superuser:
        sucursal = Sucursal.objects.get(id=id_sucursal)
        if request.method == 'GET':
            form = SucursalForm(instance=sucursal)
        else:
            form = SucursalForm(request.POST, instance=sucursal)
            if form.is_valid():
                form.save()
            return redirect('sucursal_listar')
        return render(request,'sucursal/sucursal_form.html',{'form':form})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')


# para poder eliminar una sucursal mandando su id
def sucursal_delete(request, id_sucursal):
    if request.user.is_superuser:    
        sucursal = Sucursal.objects.get(id=id_sucursal)
        if request.method == 'POST':
            sucursal.delete()
            return redirect('sucursal_listar')
        return render(request,'sucursal/sucursal_delete.html', {'sucursal':sucursal})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')
