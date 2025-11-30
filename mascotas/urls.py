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
    path('publicar/', views.MascotaCreateView.as_view(), name='publicar_mascota'),
    path('<int:pk>/editar/', views.MascotaUpdateView.as_view(), name='editar_mascota'),
    path('<int:pk>/', views.MascotaDetailView.as_view(), name='detalle_mascota'),
    path('<int:pk>/eliminar/', views.MascotaDeleteView.as_view(), name='eliminar_mascota'),
    path('<int:pk>/', views.MascotaDetailView.as_view(), name='detalle_mascota'),
    path('mis-publicaciones/', views.MascotaUserListView.as_view(), name='mis_publicaciones'),
    path('solicitudes/', views.SolicitudListView.as_view(), name='solicitudes_recibidas'),
    path('cambiar-estado/<int:pk>/<str:estado>/', views.cambiar_estado_mascota, name='cambiar_estado'), 
    path('perfil/', views.ProfileUpdateView.as_view(), name='editar_perfil'),
]