from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.

def inicio_vistaCliente(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarClientes.html", {"misclientes":losclientes})

def registrarCliente(request):
    nombre = request.POST["txtnombre"]
    f_nacimiento = request.POST["datef_nacimiento"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]

    guardarcliente = Cliente.objects.create(
        Nombre=nombre, F_nacimiento=f_nacimiento,    Telefono=telefono, Email=email, Direccion=direccion
    )  # GUARDA EL REGISTRO

    return redirect("/cliente")

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarcliente.html", {"misclientes": cliente})

def editarCliente(request):
    id_cliente = request.POST["txtid_cliente"]
    nombre = request.POST["txtnombre"]
    f_nacimiento= request.POST["datef_nacimiento"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.Nombre = nombre
    cliente.F_nacimiento = f_nacimiento
    cliente.Telefono = telefono
    cliente.Email = email
    cliente.Direccion = direccion
    cliente.save()  # guarda el registro actualizado
    return redirect("/cliente")

def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()  # borra el registro
    return redirect("/cliente")