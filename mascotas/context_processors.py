# mascotas/context_processors.py

from .models import SolicitudAdopcion
# Asegúrate de importar Mascota si tu modelo SolicitudAdopcion no tiene una relación directa con User
# pero dado que ya tienes la vista funcionando, asumimos que SolicitudAdopcion y Mascota están bien relacionadas.

def solicitudes_pendientes_count(request):
    """
    Calcula y agrega el conteo total de solicitudes recibidas por el usuario logueado 
    al contexto de la plantilla base.
    """
    count = 0
    # Solo procesar si hay un usuario logueado
    if request.user.is_authenticated:
        # Contar todas las solicitudes para las mascotas publicadas por este usuario.
        count = SolicitudAdopcion.objects.filter(
            # Filtra por la Mascota que fue publicada por el usuario actual
            mascota__publicado_por=request.user
        ).count()
        
    return {
        # Esta variable estará disponible en todos tus templates
        'total_solicitudes_recibidas': count
    }