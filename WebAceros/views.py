from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def home(request):
    return render(request,'home.html')

def contactos(request):
    return render(request,'contactos.html')

def product_list(request):
    products=Product.objects.all()
    return render(request,'productos.html',{'products':products,})

def nosotros(request):
    return render(request,'nosotros.html')

# Create your views here.
