from django.shortcuts import render, redirect
from .models import Ordenes

# Vista para listar todas las órdenes
def inicio_vistaOrden(request):
    lasordenes = Ordenes.objects.all()
    return render(request, "gestionarOrdenes.html", {"misordenes": lasordenes})

# Vista para registrar una nueva orden
def registrarOrden(request):
    id_cliente = request.POST["txtid_cliente"]
    id_producto = request.POST["txtid_producto"]
    precio = request.POST["txtprecio"]
    cantidad = request.POST["txtcantidad"]
    subtotal = float(precio) * int(cantidad)

    guardarorden = Ordenes.objects.create(
        Id_cliente=id_cliente, Id_producto=id_producto, Precio=precio, 
        Cantidad=cantidad, Subtotal=subtotal
    )  # Guarda el registro de la orden

    return redirect("/orden")

# Vista para seleccionar una orden para editarla
def seleccionarOrden(request, id_ordenes):
    orden = Ordenes.objects.get(id_ordenes=id_ordenes)
    return render(request, "editarorden.html", {"misordenes": orden})

# Vista para editar una orden existente
def editarOrden(request):
    id_ordenes = request.POST["txtid_ordenes"]
    id_cliente = request.POST["txtid_cliente"]
    id_producto = request.POST["txtid_producto"]
    precio = request.POST["txtprecio"]
    cantidad = request.POST["txtcantidad"]
    subtotal = float(precio) * int(cantidad)

    orden = Ordenes.objects.get(id_ordenes=id_ordenes)
    orden.Id_cliente = id_cliente
    orden.Id_producto = id_producto
    orden.Precio = precio
    orden.Cantidad = cantidad
    orden.Subtotal = subtotal
    orden.save()  # Guarda el registro actualizado de la orden

    return redirect("/orden")

# Vista para borrar una orden
def borrarOrden(request, id_ordenes):
    orden = Ordenes.objects.get(id_ordenes=id_ordenes)
    orden.delete()  # Borra la orden
    return redirect("/orden")
