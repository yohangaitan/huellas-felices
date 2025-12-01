# blog/admin.py

from django.contrib import admin
from .models import Articulo

# 📝 Clase ArticuloAdmin para personalizar la interfaz de administración
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista de artículos
    list_display = ('titulo', 'categoria', 'fecha_publicacion', 'publicado') 
    
    # Filtros laterales para búsqueda rápida
    list_filter = ('categoria', 'fecha_publicacion', 'publicado')
    
    # Campos que permiten la edición directa en la lista (útil para el estado 'publicado')
    list_editable = ('publicado',) 
    
    # Campos de búsqueda rápida
    search_fields = ('titulo', 'contenido')
    
    # Pre-poblado automático del slug (se genera a partir del título al escribir)
    prepopulated_fields = {'slug': ('titulo',)} 
    
    # Organización de los campos en el formulario de edición
    fieldsets = (
        (None, {
            'fields': ('titulo', 'slug', 'categoria', 'publicado')
        }),
        ('Contenido del Artículo', {
            'fields': ('descripcion_corta', 'contenido', 'imagen_principal')
        }),
    )