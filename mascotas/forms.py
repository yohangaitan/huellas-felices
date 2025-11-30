# mascotas/forms.py

from django import forms
from .models import Mascota, SolicitudAdopcion, UserProfile

class MascotaForm(forms.ModelForm):
    # Sobreescribimos el campo descripcion para usar un widget Textarea 
    # y darle un placeholder, mejorando la UX.
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe su historia, personalidad, y cuidados especiales.'}),
        label='Descripción Completa'
    )
    
    class Meta:
        model = Mascota
        #  CAMPOS CORREGIDOS: Coinciden con el modelo (models.py)
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
        ]
        
        #  ETIQUETAS (LABELS) CORREGIDAS
        labels = {
            'edad': 'Edad Clasificada (Cachorro, Joven, Adulto)', # Etiqueta actualizada para el nuevo tipo de campo
            'region': 'Provincia o Región',
            'imagen': 'Foto Principal', # Corregido el nombre
        }
        
        # Opcional: Para asegurar que los campos de tipo choice (select) usen las clases correctas
        widgets = {
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'tamano': forms.Select(attrs={'class': 'form-select'}),
            'edad': forms.Select(attrs={'class': 'form-select'}),
            'region': forms.Select(attrs={'class': 'form-select'}),
        }

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['nombre_completo', 'correo_electronico', 'telefono', 'mensaje']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono (opcional)'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu mensaje...'})
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Solo vamos a permitir editar el teléfono
        fields = ['telefono_whatsapp'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar clases de Tailwind/CSS
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-orange-500 focus:border-orange-500'
            })