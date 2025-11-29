# mascotas/models.py

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#Create your models here.
class Mascota(models.Model):
    # --- Opciones (Choices) para asegurar datos consistentes ---
    
    ESPECIE_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]
    TAMANO_CHOICES = [
        ('P', 'Pequeño'),
        ('M', 'Mediano'),
        ('G', 'Grande'),
    ]
    ESTADO_CHOICES = [
        ('D', 'Disponible'),
        ('P', 'En Proceso'),
        ('A', 'Adoptado'),
    ]
    
    # --- Información Básica ---
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=5, choices=ESPECIE_CHOICES)
    raza = models.CharField(max_length=100, blank=True, default='Mestizo')
    genero = models.CharField(max_length=1, choices=[('M', 'Macho'), ('H', 'Hembra')])
    
    # --- Características ---
    edad_anos = models.IntegerField(verbose_name="Edad (años aproximados)")
    tamano = models.CharField(max_length=1, choices=TAMANO_CHOICES)
    descripcion = models.TextField(help_text="Historia, personalidad y necesidades de la mascota.")
    
    # --- Medios y Control ---
    imagen_principal = models.ImageField(
        upload_to='mascotas_fotos/',
        help_text="Foto principal de la mascota."
    )
    
    # --- Adopción y Publicación ---
    estado_adopcion = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='D')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    # Relación con el publicador (Rescatista/Organización)
    # Por ahora, usamos el modelo de Usuario por defecto de Django
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
        ordering = ['-fecha_publicacion'] # Ordenar por las más nuevas primero

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        # Esta función será útil más adelante para redirigir tras la creación
        # Necesitaremos crear la URL 'detalle_mascota' primero
        return reverse('mascotas:detalle', args=[str(self.id)])