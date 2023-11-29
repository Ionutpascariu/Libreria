from typing import Any
from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripción',null=True)

    def __str__(self):
        fila = "Título: " + self.titulo + " - " + "Descripcion: " + self.descripcion
        return fila
    
#Este trozo ayuda a eliminar tambíen las imagenes de la base de datos una vez borrado
    def delete(self, using=None, keep_parents= False ):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()