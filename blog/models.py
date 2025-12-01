from django.db import models
from django.utils.text import slugify

# Create your models here.

class Articulo(models.Model):
    CATEGORIA_CHOICES = (
    ('ADOPCION', 'Adopción de Mascotas'),
    ('PERROS', 'Cuidado de Perros'),
    ('GATOS', 'Cuidado de Gatos'),
)
    
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='ADOPCION')
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen_principal = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    descripcion_corta = models.TextField(max_length=300, help_text="Máximo 300 caracteres para la vista previa.")
    publicado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name_plural = "Artículos"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo