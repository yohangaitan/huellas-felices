from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

# Modelos y formularios
from .models import Mascota, UserProfile
from .forms import MascotaForm, SolicitudAdopcionForm, UserProfileForm


# -------------------------
# 1. Vista de Inicio
# -------------------------
class HomeView(TemplateView):
    template_name = 'mascotas/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['mascotas_disponibles_count'] = Mascota.objects.filter(
            estado_adopcion='D'
        ).count()

        context['mascotas_destacadas'] = Mascota.objects.filter(
            estado_adopcion='D'
        ).order_by('-fecha_publicacion')[:4]

        return context


# -------------------------
# 2. Listado Base + Perros + Gatos
# -------------------------
class MascotaBaseListView(ListView):
    model = Mascota
    context_object_name = 'mascotas_disponibles'
    template_name = 'mascotas/listado_base.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = Mascota.objects.filter(
            estado_adopcion='D'
        ).order_by('-fecha_publicacion')

        query = self.request.GET.get('q')
        tamano = self.request.GET.get('tamano')
        edad = self.request.GET.get('edad')
        region = self.request.GET.get('region')
        genero = self.request.GET.get('genero')
        color = self.request.GET.get('color')

        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(raza__icontains=query) |
                Q(descripcion__icontains=query)
            )

        if tamano:
            queryset = queryset.filter(tamano=tamano)
        if edad:
            queryset = queryset.filter(edad=edad)
        if region:
            queryset = queryset.filter(region=region)
        if genero:
            queryset = queryset.filter(genero=genero)
        if color:
            queryset = queryset.filter(color=color)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['tamano_seleccionado'] = self.request.GET.get('tamano', '')
        context['edad_seleccionada'] = self.request.GET.get('edad', '')
        context['region_seleccionada'] = self.request.GET.get('region', '')
        context['sexo_seleccionado'] = self.request.GET.get('genero', '')
        context['color_seleccionado'] = self.request.GET.get('color', '')

        context['TAMANO_CHOICES'] = Mascota.TAMANO_CHOICES
        context['EDAD_CHOICES'] = Mascota.EDAD_CHOICES
        context['REGION_CHOICES'] = Mascota.REGION_CHOICES
        context['SEXO_CHOICES'] = Mascota.GENERO_CHOICES
        context['COLOR_CHOICES'] = Mascota.COLOR_CHOICES

        return context


class PerroListView(MascotaBaseListView):
    def get_queryset(self):
        return super().get_queryset().filter(especie='Perro')


class GatoListView(MascotaBaseListView):
    def get_queryset(self):
        return super().get_queryset().filter(especie='Gato')


# -------------------------
# 3. Detalle de Mascota + Solicitud
# -------------------------
class MascotaDetailView(DetailView):
    model = Mascota
    template_name = 'mascotas/detalle.html'
    context_object_name = 'mascota'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SolicitudAdopcionForm(initial={
            'nombre_completo': self.request.user.get_full_name() if self.request.user.is_authenticated else '',
            'correo_electronico': self.request.user.email if self.request.user.is_authenticated else '',
        })
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = SolicitudAdopcionForm(request.POST)

        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.mascota = self.object

            if request.user.is_authenticated:
                solicitud.solicitante = request.user

            solicitud.save()
            return redirect(reverse('mascotas:detalle_mascota', kwargs={'pk': self.object.pk}))

        context = self.get_context_data(object=self.object)
        context['form'] = form
        return self.render_to_response(context)


# -------------------------
# 4. Crear Mascota (usa publicar_mascota.html)
# -------------------------
class MascotaCreateView(LoginRequiredMixin, CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/publicar_mascota.html'
    success_url = reverse_lazy('mascotas:home')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Publicar Mascota"
        context["boton_texto"] = "Subir Mascota"
        return context

    def form_valid(self, form):
        form.instance.publicado_por = self.request.user
        form.instance.estado_adopcion = 'D'
        return super().form_valid(form)


# -------------------------
# Registro de usuarios
# -------------------------
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


# -------------------------
# 5. Editar Mascota (usa mismo template que publicar)
# -------------------------
class MascotaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/publicar_mascota.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar Mascota"
        context["boton_texto"] = "Guardar Cambios"
        return context

    def get_success_url(self):
        return reverse_lazy('mascotas:detalle_mascota', kwargs={'pk': self.object.pk})

    def test_func(self):
        mascota = self.get_object()
        return self.request.user == mascota.publicado_por


# -------------------------
# 6. Eliminar Mascota
# -------------------------
class MascotaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mascota
    template_name = 'mascotas/eliminar_mascota.html'
    success_url = reverse_lazy('mascotas:home')

    def test_func(self):
        mascota = self.get_object()
        return self.request.user == mascota.publicado_por


# -------------------------
# 7. Mis Publicaciones
# -------------------------
class MascotaUserListView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'mascotas/mis_publicaciones.html'
    context_object_name = 'mis_mascotas'

    def get_queryset(self):
        return Mascota.objects.filter(
            publicado_por=self.request.user
        ).annotate(
            solicitudes_count=Count('solicitudes')
        ).order_by('-fecha_publicacion')


# -------------------------
# 8. Cambiar estado
# -------------------------
@login_required
def cambiar_estado_mascota(request, pk, estado):
    mascota = get_object_or_404(Mascota, pk=pk)

    if mascota.publicado_por != request.user:
        return HttpResponseForbidden("No tienes permiso para modificar esta mascota.")

    if estado in ['D', 'P', 'A']:
        mascota.estado_adopcion = estado
        mascota.save()

    return redirect(reverse('mascotas:detalle_mascota', kwargs={'pk': pk}))


# -------------------------
# 9. Actualizar perfil
# -------------------------
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'mascotas/profile_form.html'
    success_url = reverse_lazy('mascotas:mis_publicaciones')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, "Tu perfil ha sido actualizado con éxito.")
        return super().form_valid(form)
