from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bd(request):
    if request.method == 'POST':
        print("Método post")
        print(request.POST['archivo'])
    else:
        print("Método get")
    return render(request, 'forms/form_BD.html')
