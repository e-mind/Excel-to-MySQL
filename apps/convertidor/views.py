import re
from django.shortcuts import render
from django.http import HttpResponse
patron_nombre = re.compile('^[\w][^.!¡´[]()":,]*')
# Create your views here.
def bd(request):
    return render( request, 'convertidor/form_BD.html')

def index(request):
    return render( request, 'home.html')
