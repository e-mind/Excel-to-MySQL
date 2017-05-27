from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import os
from apps.encriptador import main
from apps.encriptador.forms import DataForm

# Create your views here.
def entrada(request):
    if request.method == 'POST':
        final0 = main.proceso(request.POST['desencriptar'])
        final = main.proceso(request.POST['encriptar'])
        return render(request, 'encriptador/entrada.html', {'final':final, 'final0':final0})

    return render(request, 'encriptador/entrada.html')
