from django.db import models

class Producto(models.Model):
    artista = models.CharField(max_length=50, default='Desconocido')
    nombreprod = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombreprod
    

class Persona(models.Model):
    rut=models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50,null=False)
    edad=models.IntegerField(null=False)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"