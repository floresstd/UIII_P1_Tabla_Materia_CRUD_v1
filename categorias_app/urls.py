from django.urls import path
from categorias_app import views

urlpatterns = [
    path('categoria', views.inicio_vistaCategoria, name="inicio_vistaCategoria"),
    path("registrarCategoria/", views.registrarCategoria, name="registrarCategoria"),  # Ruta para registrar una categoría
    path("seleccionarCategoria/<int:id_categoria>/", views.seleccionarCategoria, name="seleccionarCategoria"),  # Ruta para seleccionar una categoría
    path("editarCategoria/", views.editarCategoria, name="editarCategoria"),  # Ruta para editar una categoría
    path("borrarCategoria/<int:id_categoria>/", views.borrarCategoria, name="borrarCategoria"),  # Ruta para borrar una categoría
]
