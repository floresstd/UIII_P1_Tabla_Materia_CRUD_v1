from django.urls import path
from ordenes_app import views  # Asegúrate de que este import sea correcto según el nombre de tu app

urlpatterns = [
    path('orden', views.inicio_vistaOrden, name="inicio_vistaOrden"),  # Vista para listar todas las órdenes
    path("registrarOrden/", views.registrarOrden, name="registrarOrden"),  # Ruta para registrar una nueva orden
    path("seleccionarOrden/<int:id_ordenes>/", views.seleccionarOrden, name="seleccionarOrden"),  # Ruta para seleccionar una orden
    path("editarOrden/", views.editarOrden, name="editarOrden"),  # Ruta para editar una orden
    path("borrarOrden/<int:id_ordenes>/", views.borrarOrden, name="borrarOrden"),  # Ruta para borrar una orden
]
