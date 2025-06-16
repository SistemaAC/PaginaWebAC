from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactos/', views.contactos, name='contactos'),
    path('productos/', views.productos, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    
   # path('contactos/',views.contactos, name = 'contactos'),
]
