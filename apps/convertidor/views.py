from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bd(request):
    return render( request, 'forms/form_BD.html')
