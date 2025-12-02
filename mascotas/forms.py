# mascotas/forms.py

from django import forms
from .models import Mascota, SolicitudAdopcion, UserProfile

TEXT_INPUT_CLASSES = "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-teal-500 focus:border-teal-500 transition duration-150"
class MascotaForm(forms.ModelForm):
    # Sobreescribimos el campo descripcion para usar un widget Textarea 
    # y darle un placeholder, mejorando la UX.
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe su historia, personalidad, y cuidados especiales.','class': TEXT_INPUT_CLASSES + ' h-32'}),
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
            'imagen': 'Foto Principal',
            'nombre': 'Nombre',
            'raza': 'Raza (Ej: Mestizo)',
        }
        
        # Opcional: Para asegurar que los campos de tipo choice (select) usen las clases correctas
        widgets = {
            'especie': forms.Select(attrs={'class': TEXT_INPUT_CLASSES}),
            'genero': forms.Select(attrs={'class': TEXT_INPUT_CLASSES}),
            'tamano': forms.Select(attrs={'class': TEXT_INPUT_CLASSES}),
            'edad': forms.Select(attrs={'class': TEXT_INPUT_CLASSES}),
            'region': forms.Select(attrs={'class': TEXT_INPUT_CLASSES}),
            'imagen': forms.FileInput(attrs={'class': 'w-full text-gray-700 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-teal-50 file:text-teal-700 hover:file:bg-teal-100 transition'}),
        }

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['nombre_completo', 'correo_electronico', 'telefono', 'mensaje']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': TEXT_INPUT_CLASSES, 'placeholder': 'Tu nombre completo'}),
            'correo_electronico': forms.EmailInput(attrs={'class': TEXT_INPUT_CLASSES, 'placeholder': 'Tu correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': TEXT_INPUT_CLASSES, 'placeholder': 'Teléfono (opcional)'}),
            'mensaje': forms.Textarea(attrs={'class': TEXT_INPUT_CLASSES, 'rows': 4, 'placeholder': 'Escribe tu mensaje...'})
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