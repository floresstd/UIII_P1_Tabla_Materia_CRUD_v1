from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=255)
    F_nacimiento = models.DateField(null=True, blank=True)
    Telefono = models.CharField(max_length=15)
    Email = models.EmailField(max_length=255)
    Direccion = models.TextField()
    

    def __str__(self):
        return self.Nombre
