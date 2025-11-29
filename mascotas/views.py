from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Mascota
from django.db.models import Q

# Create your views here.
# 1. Vista de Inicio (HomeView)
# Muestra una página estática, pero podemos pasarle datos si queremos.
class HomeView(TemplateView):
    template_name = 'mascotas/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Opcional: pasar las últimas 4 mascotas disponibles al contexto
        context['ultimas_mascotas'] = Mascota.objects.filter(
            estado_adopcion='D'
        ).order_by('-fecha_publicacion')[:4]
        return context

# 2. Vistas de Listado (Perros y Gatos)

class MascotaBaseListView(ListView):
    """Clase base para el listado, define parámetros comunes."""
    model = Mascota
    context_object_name = 'mascotas_disponibles' # Nombre que usaremos en el template
    template_name = 'mascotas/listado_base.html'
    paginate_by = 12 # Paginación opcional

    def get_queryset(self):
        # Aseguramos que solo se muestren las disponibles
        return Mascota.objects.filter(estado_adopcion='D').order_by('-fecha_publicacion')

class PerroListView(MascotaBaseListView):
    """Muestra solo perros disponibles."""
    def get_queryset(self):
        # Filtra el queryset base para solo incluir perros
        return super().get_queryset().filter(especie='Perro')

class GatoListView(MascotaBaseListView):
    """Muestra solo gatos disponibles."""
    def get_queryset(self):
        # Filtra el queryset base para solo incluir gatos
        return super().get_queryset().filter(especie='Gato')
    

# 3. Vista de Detalle de Mascota
class MascotaDetailView(DetailView):
    """Muestra la información completa de una mascota."""
    model = Mascota
    template_name = 'mascotas/detalle.html'
    context_object_name = 'mascota' # El objeto se llamará 'mascota' en la plantilla