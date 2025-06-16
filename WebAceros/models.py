from django.db import models

class Tabla_test(models.Model):
    columna_uno=models.CharField(max_length=200)
    columna_dos=models.CharField(max_length=200)
    columna_tres=models.CharField(max_length=200)
# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    code=models.CharField(max_length=15)
    fecha_crea=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField()
    def __str__(self):
        return self.nombre
class Product(models.Model):
    nombre= models.CharField(max_length=100)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    caracter=models.TextField()
    descripcion=models.TextField()
    presentacion=models.TextField()
    imagen = models.DecimalField(max_digits=10,decimal_places=True)
    fecha_crea=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField()
    def __str__(self):
        return self.nombre
class Sucursales(models.Model):
    nombre= models.CharField(max_length=100)
    direccion= models.TextField()
    telefono= models.IntegerField(max_length=9)
    coordenada= models.TextField()
    fecha_crea=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField()
    def __str__(self):
        return self.nombre