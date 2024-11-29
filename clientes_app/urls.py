from django.urls import path
from clientes_app import views
urlpatterns = [
    path('cliente', views.inicio_vistaCliente, name="inicio_vistaCliente"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),  # Ruta para registrar un cliente
    path("seleccionarCliente/<id_cliente>/", views.seleccionarCliente, name="seleccionarCliente"),  # Ruta para seleccionar un cliente
    path("editarCliente/", views.editarCliente, name="editarCliente"),  # Ruta para editar un cliente
    path("borrarCliente/<int:id_cliente>/", views.borrarCliente, name="borrarCliente"),  # Ruta para borrar un cliente
]
