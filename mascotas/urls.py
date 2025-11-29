from django.urls import path
from . import views

# Define el nombre de la aplicación para hacer referencia a las URLs fácilmente
app_name = 'mascotas'

urlpatterns = [
    # Vista de Inicio: Muestra un resumen general
    path('', views.HomeView.as_view(), name='home'),
    
    # Listados de Mascotas (filtrados por especie)
    path('perros/', views.PerroListView.as_view(), name='listado_perros'),
    path('gatos/', views.GatoListView.as_view(), name='listado_gatos'),
    # Detalle de una mascota por su ID (Primary Key: pk)
    path('detalle/<int:pk>/', views.MascotaDetailView.as_view(), name='detalle'),
]