from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Eliminamos la importación de reverse ya que no se usa en este archivo

# --- Opciones de Choices (Fuera de las clases si son compartidas) ---
# Aunque tienes duplicadas estas en Mascota, las mantendré comentadas para no romper nada

# Create your models here.
class Mascota(models.Model):
    # --- 1. Definición de Choices (Internas) ---
    TAMANO_CHOICES = [
        ('P', 'Pequeño'),
        ('M', 'Mediano'),
        ('G', 'Grande'),
    ]
    
    EDAD_CHOICES = [
        ('C', 'Cachorro (0-1 año)'),
        ('J', 'Joven (1-7 años)'),
        ('A', 'Adulto (+7 años)'),
    ]

    REGION_CHOICES = [
        ('Panamá', 'Panamá'),
        ('Panamá Oeste', 'Panamá Oeste'),
        ('Colón', 'Colón'),
        ('Los Santos', 'Los Santos'),
        ('Coclé', 'Coclé'),
        ('Veraguas', 'Veraguas'),
        ('Darién', 'Darién'),
        ('Chiriquí', 'Chiriquí'),
    ]
    
    GENERO_CHOICES = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    
    ESPECIE_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]

    ESTADO_CHOICES = [
        ('D', 'Disponible'),
        ('P', 'Pendiente de adopción'),
        ('A', 'Adoptado'),
    ]

    # --- 2. Campos del Modelo ---
    
    publicado_por = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='mascotas_publicadas'
    )
    
    nombre = models.CharField(max_length=100)
    
    # Campos que usan los Choices
    especie = models.CharField(max_length=5, choices=ESPECIE_CHOICES)
    genero = models.CharField(max_length=6, choices=GENERO_CHOICES)
    tamano = models.CharField(max_length=1, choices=TAMANO_CHOICES)
    edad = models.CharField(max_length=1, choices=EDAD_CHOICES)
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    estado_adopcion = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='D')
    
    # Otros campos
    raza = models.CharField(max_length=100, default='Mestizo', blank=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='mascotas_fotos/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
        ordering = ['-fecha_publicacion']
    
# ----------------------------------------------------------------------
# ELIMINÉ LA CLASE SolicitudAdopcion ANIDADA Y LA DEFINICIÓN DUPLICADA
# AHORA SÓLO TENEMOS UNA DEFINICIÓN VÁLIDA:
# ----------------------------------------------------------------------
class SolicitudAdopcion(models.Model):
    # La relación inversa se llama 'solicitudes'
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE, related_name='solicitudes')
    
    # Usuario solicitante.
    solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='solicitudes_enviadas', null=True, blank=True)
    
    nombre_completo = models.CharField(max_length=150)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    mensaje = models.TextField(help_text="Cuéntale al publicador por qué quieres adoptar a esta mascota.")
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Solicitud de {self.nombre_completo} para {self.mascota.nombre}"

    class Meta:
        verbose_name = "Solicitud de Adopción"
        verbose_name_plural = "Solicitudes de Adopción"
        ordering = ['-fecha_solicitud']

# Perfil de Usuario
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    
    telefono_whatsapp = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        help_text="Tu número de teléfono para ser contactado por WhatsApp (ej: 5076xxxxxx)"
    )
    
    def __str__(self):
        return f"Perfil de {self.user.username}"