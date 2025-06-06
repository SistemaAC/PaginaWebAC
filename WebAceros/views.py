from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')

def contactos(request):
    return render(request,'contactos.html')

def productos(request):
    return render(request,'productos.html')

def Nosotros(request):
    return render(request,'nosotros.html')

# Create your views here.
