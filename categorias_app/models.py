from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=255)

    def __str__(self):
        return self.Nombre
