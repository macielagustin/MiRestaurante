from django.db import models

# Create your models here.

class Pedido(models.Model):
    nombre= models.CharField(max_length=80, unique=True, verbose_name="Nombre de Pedido")

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de Cliente")
    pedido = models.ForeignKey(Pedido,on_delete=models.PROTECT)
    email = models.EmailField(max_length=250, unique= True)
    imagen= models.ImageField(upload_to="clientes/", null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class FAQ(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta
