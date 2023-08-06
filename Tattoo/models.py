from django.db import models

# Create your models here.

class Tatuador(models.Model):
    nombre =models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9,)
    dni = models.CharField(max_length=8,)
    yape = models.ImageField(upload_to='imagenes/')
    ig = models.URLField()

    def __str__(self):
        txt ="{0} {1}"
        return txt.format(self.nombre, self.apellido)

class ImagenTattoos(models.Model):
    
    tatuador =models.ForeignKey(Tatuador,null=False,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/')
    titulo =models.CharField(max_length=50, default='titulo predeterminada')
    descripcion = models.CharField(max_length=100, default='Descripción predeterminada')

    def __str__(self):
        txt ="Imagen N: {0} de {1}"
        return txt.format(self.imagen, self.tatuador)

class Usuario(models.Model):
    nombre =models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9,)

    def __str__(self):
        txt ="{0} {1}"
        return txt.format(self.nombre, self.apellido)
    