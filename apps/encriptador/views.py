from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import os
from apps.encriptador import main
from apps.encriptador.forms import DataForm

# Create your views here.
def entrada(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            frase = form.cleaned_data['datos']
            final = main.proceso(frase)
            print (final)
            return render(request, 'encriptador/salida.html', {'final':final})

    return render(request, 'encriptador/entrada.html')

def salida(request, final= 'carlos'):
    if request.method == 'GET':
        form = final
    else:
        form = DataForm(request.POST)
        if form.is_valid():
            frase = form.cleaned_data['datos']
            final = main.proceso(frase)
            print (final)
            return HttpResponseRedirect('/encriptador/')

    return render(request, 'encriptador/salida.html')
