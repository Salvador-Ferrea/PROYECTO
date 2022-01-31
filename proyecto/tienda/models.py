from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100, verbose_name='Categoria')

    def __str__(self):
        fila = self.nombre
        return fila

class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100, verbose_name='Título',)
    precio= models.FloatField(verbose_name='Precio')
    stock= models.IntegerField(verbose_name='Stock')
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Categoría')

    def __str__(self):
        fila = "Nombre: " + self.nombre
        return fila
