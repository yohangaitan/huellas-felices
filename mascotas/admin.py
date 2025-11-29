from django.contrib import admin
from .models import Mascota

# Register your models here.
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'estado_adopcion', 'publicado_por', 'fecha_publicacion')
    list_filter = ('especie', 'estado_adopcion', 'tamano', 'fecha_publicacion')
    search_fields = ('nombre', 'raza', 'descripcion')