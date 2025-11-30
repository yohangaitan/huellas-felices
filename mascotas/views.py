from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views.generic.edit import UpdateView
from django.contrib import messages
# Importar modelos y formularios
from .models import Mascota, SolicitudAdopcion, UserProfile
from .forms import MascotaForm, SolicitudAdopcionForm, UserProfileForm


# 1. Vista de Inicio (HomeView)
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
    """Clase base para el listado, define parámetros comunes e incorpora filtros."""
    model = Mascota
    context_object_name = 'mascotas_disponibles'
    template_name = 'mascotas/listado_base.html'
    paginate_by = 12

    def get_queryset(self):
        # 1. Empieza con todas las mascotas disponibles
        queryset = Mascota.objects.filter(estado_adopcion='D').order_by('-fecha_publicacion')
        
        # 2. Obtener parámetros de búsqueda de la URL (GET)
        query = self.request.GET.get('q')
        tamano = self.request.GET.get('tamano')
        edad = self.request.GET.get('edad')
        region = self.request.GET.get('region')
        
        # --- Aplicar Búsqueda por Texto (Q object para OR) ---
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(raza__icontains=query) |
                Q(descripcion__icontains=query)
            )
            
        # --- Aplicar Filtros Específicos (solo si tienen valor) ---
        if tamano:
            queryset = queryset.filter(tamano=tamano)
        
        if edad:
            queryset = queryset.filter(edad=edad)
            
        if region:
            queryset = queryset.filter(region=region)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasar los valores de filtro para mantenerlos en el formulario después de la búsqueda
        context['query'] = self.request.GET.get('q', '')
        context['tamano_seleccionado'] = self.request.GET.get('tamano', '')
        context['edad_seleccionada'] = self.request.GET.get('edad', '')
        context['region_seleccionada'] = self.request.GET.get('region', '')
        
        # Pasar los Choices del modelo para crear los select
        context['TAMANO_CHOICES'] = Mascota.TAMANO_CHOICES
        context['EDAD_CHOICES'] = Mascota.EDAD_CHOICES
        context['REGION_CHOICES'] = Mascota.REGION_CHOICES
        return context


class PerroListView(MascotaBaseListView):
    """Muestra solo perros disponibles (hereda la lógica de filtrado)."""
    def get_queryset(self):
        # Filtra por especie='Perro' además de todos los filtros de la clase base
        return super().get_queryset().filter(especie='Perro')

class GatoListView(MascotaBaseListView):
    """Muestra solo gatos disponibles (hereda la lógica de filtrado)."""
    def get_queryset(self):
        # Filtra por especie='Gato' además de todos los filtros de la clase base
        return super().get_queryset().filter(especie='Gato')
    

# 3. Vista de Detalle de Mascota (ACTUALIZADA con manejo de POST para solicitud)
class MascotaDetailView(DetailView):
    """Muestra la información completa de una mascota y el formulario de solicitud."""
    model = Mascota
    template_name = 'mascotas/detalle.html'
    context_object_name = 'mascota'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasa el formulario de solicitud al contexto (GET)
        context['form'] = SolicitudAdopcionForm(initial={
            'nombre_completo': self.request.user.get_full_name() if self.request.user.is_authenticated else '',
            'correo_electronico': self.request.user.email if self.request.user.is_authenticated else '',
        })
        return context

    def post(self, request, *args, **kwargs):
        # Manejar el envío del formulario de solicitud (Método POST)
        self.object = self.get_object() # Obtener la mascota
        form = SolicitudAdopcionForm(request.POST)

        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.mascota = self.object
            
            # Asignar el usuario logueado como solicitante
            if request.user.is_authenticated:
                solicitud.solicitante = request.user
            
            solicitud.save()
            
            # Redirigir al detalle de la mascota después del envío
            return redirect(reverse('mascotas:detalle_mascota', kwargs={'pk': self.object.pk}))
        
        # Si el formulario no es válido, volvemos a renderizar
        context = self.get_context_data(object=self.object)
        context['form'] = form
        return self.render_to_response(context)


# 4. Vista para Publicar una Nueva Mascota
class MascotaCreateView(LoginRequiredMixin, CreateView):
    """Permite a usuarios logueados publicar una nueva mascota."""
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/publicar_mascota.html'
    success_url = reverse_lazy('mascotas:home')
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.publicado_por = self.request.user
        form.instance.estado_adopcion = 'D'
        return super().form_valid(form)
    
# Para el registro de nuevos usuarios
class SignUpView(CreateView):
    """Permite crear un nuevo usuario usando el formulario estándar de Django."""
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# MascotaUpdateView
class MascotaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mascota
    fields = [
        'nombre', 
        'especie',
        'raza', 
        'genero',
        'edad',
        'region',
        'tamano', 
        'descripcion', 
        'imagen',
        'estado_adopcion',
    ]
    template_name = 'mascotas/publicar_mascota.html'
    
    def get_success_url(self):
        return reverse_lazy('mascotas:detalle_mascota', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        mascota = self.get_object()
        return self.request.user == mascota.publicado_por
    
# MascotaDeleteView
class MascotaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mascota
    template_name = 'mascotas/eliminar_mascota.html'
    success_url = reverse_lazy('mascotas:home')
    
    def test_func(self):
        mascota = self.get_object()
        return self.request.user == mascota.publicado_por
    
# MascotaUserListView
class MascotaUserListView(LoginRequiredMixin, ListView):
    """Muestra solo las mascotas publicadas por el usuario actual y cuenta sus solicitudes."""
    model = Mascota
    template_name = 'mascotas/mis_publicaciones.html'
    context_object_name = 'mis_mascotas'
    
    def get_queryset(self):
        # Filtra por 'publicado_por' y ANOTA el conteo de solicitudes.
        return Mascota.objects.filter(publicado_por=self.request.user).annotate(
            # ⬅️ 2. USAR ANNOTATE
            # 'solicitudes_count' será el nuevo campo accesible en el template.
            # 'solicitudadopcion' es el nombre del modelo de solicitudes en minúsculas (o el related_name).
            solicitudes_count=Count('solicitudadopcion') 
        ).order_by('-fecha_publicacion')
    
# 6. Vista de Listado de Solicitudes Recibidas
class SolicitudListView(LoginRequiredMixin, ListView):
    """Muestra todas las solicitudes enviadas para las mascotas del usuario actual."""
    model = SolicitudAdopcion
    template_name = 'mascotas/solicitudes_recibidas.html'
    context_object_name = 'solicitudes'
    
    def get_queryset(self):
        # Filtra las solicitudes: solo aquellas cuya mascota fue publicada por el usuario actual
        # Usamos el campo 'mascota' y luego el campo 'publicado_por' dentro de la mascota
        return SolicitudAdopcion.objects.filter(
            mascota__publicado_por=self.request.user
        ).select_related('mascota').order_by('-fecha_solicitud')
    
@login_required
def cambiar_estado_mascota(request, pk, estado):
    """
    Vista simple para cambiar el estado de una mascota (D, P, A).
    Permite al publicador marcar como 'Pendiente' o 'Adoptado'.
    """
    mascota = get_object_or_404(Mascota, pk=pk)

    # 1. Verificar Permisos: Solo el publicador puede cambiar el estado.
    if mascota.publicado_por != request.user:
        return HttpResponseForbidden("No tienes permiso para modificar esta mascota.")

    # 2. Aplicar el nuevo estado si es válido.
    estados_validos = ['D', 'P', 'A']
    if estado in estados_validos:
        mascota.estado_adopcion = estado
        mascota.save()

    # 3. Redirigir de vuelta a la página de detalle de la mascota
    return redirect(reverse('mascotas:detalle_mascota', kwargs={'pk': pk}))

# 📢 NUEVA VISTA: ProfileUpdateView
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Permite al usuario logueado editar su propio perfil."""
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'mascotas/profile_form.html'
    # Redirigir a "Mis Publicaciones" después de guardar
    success_url = reverse_lazy('mascotas:mis_publicaciones') 
    
    def get_object(self, queryset=None):
        # Esta es la parte CLAVE: asegura que solo se edite el perfil del usuario actual
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, "Tu perfil (incluido tu número de WhatsApp) ha sido actualizado con éxito.")
        return super().form_valid(form)