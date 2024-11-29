from django.db import models

# Create your models here.
from django.db import models

class Ordenes(models.Model):
    id_ordenes = models.AutoField(primary_key=True) 
    Id_cliente = models.IntegerField() 
    Id_producto = models.IntegerField() 
    Precio = models.DecimalField(max_digits=6, decimal_places=2)
    Cantidad = models.IntegerField() 
    Subtotal = Precio * Cantidad

    def __str__(self):
        return self.id_ordenes
