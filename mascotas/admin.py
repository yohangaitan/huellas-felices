from django.contrib import admin
from .models import Mascota, SolicitudAdopcion, UserProfile

# Register your models here.
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'estado_adopcion', 'publicado_por', 'fecha_publicacion')
    list_filter = ('especie', 'estado_adopcion', 'tamano', 'fecha_publicacion')
    search_fields = ('nombre', 'raza', 'descripcion')

# 2. Registrar SolicitudAdopcion
admin.site.register(SolicitudAdopcion)

# 📢 3. REGISTRAR EL NUEVO MODELO USERPROFILE
admin.site.register(UserProfile)