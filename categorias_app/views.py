from django.shortcuts import render, redirect
from .models import Categoria

# Vista para listar las categorías
def inicio_vistaCategoria(request):
    lascategorias = Categoria.objects.all()
    return render(request, "gestionarCategorias.html", {"miscategorias": lascategorias})

# Vista para registrar una nueva categoría
def registrarCategoria(request):
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]

    guardarcategoria = Categoria.objects.create(
        Nombre=nombre, Descripcion=descripcion
    )  # Guarda el registro

    return redirect("/categoria")

# Vista para seleccionar una categoría para editarla
def seleccionarCategoria(request, id_categoria):
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    return render(request, "editarcategoria.html", {"miscategorias": categoria})

# Vista para editar una categoría existente
def editarCategoria(request):
    id_categoria = request.POST["txtid_categoria"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    categoria.Nombre = nombre
    categoria.Descripcion = descripcion
    categoria.save()  # Guarda el registro actualizado
    return redirect("/categoria")

# Vista para borrar una categoría
def borrarCategoria(request, id_categoria):
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    categoria.delete()  # Borra el registro
    return redirect("/categoria")
