🏡 Huellas Felices: Plataforma de Adopción de Mascotas

Huellas Felices es una aplicación web desarrollada con Django que digitaliza el proceso de publicación y adopción de mascotas. Su propósito es conectar de forma moderna y simple a quienes buscan un nuevo compañero peludo y a quienes necesitan encontrar un hogar seguro para sus animales.

✨ Características Clave del Proyecto

Gestión de Usuarios:
Los usuarios pueden registrarse, iniciar sesión y administrar sus perfiles y publicaciones.

Publicación Detallada de Mascotas:
Permite agregar tipo de mascota, tamaño, edad, provincia, descripción e imágenes.

Navegación Intuitiva:
Listados separados para perros y gatos, además de una vista detallada para cada mascota.

Integración de Contacto:
Se facilita la comunicación directa entre adoptante y publicador mediante enlaces de contacto.

Blog Opcional:
Incluye sección para noticias, consejos y contenido educativo sobre adopciones.

💻 Tecnologías Utilizadas
Categoría	Tecnología	Uso Principal
Backend	Python 3.x, Django 5.x	Lógica, ORM, vistas, autenticación
Frontend	HTML5, Tailwind CSS	Diseño responsivo y estilización moderna
Base de Datos	SQLite3 (Desarrollo)	Almacenamiento local y gestión de modelos
Estilos	Bootstrap Icons, Widget Tweaks	Iconos y personalización de formularios
🚀 Instalación y Puesta en Marcha (Local)

Sigue estos pasos para ejecutar el proyecto en tu máquina.

1. Requisitos Previos

Necesitas tener instalado:

Python 3.10 o superior

Git

2. Clonar el Repositorio
git clone https://github.com/tu-usuario/huellas-felices.git
cd huellas-felices

3. Configurar el Entorno Virtual
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
# .\venv\Scripts\Activate

# macOS / Linux:
source venv/bin/activate

4. Instalar Dependencias

El proyecto utiliza librerías como Django, Pillow y django-widget-tweaks.

pip install -r requirements.txt

5. Configurar Base de Datos y Superusuario
# Aplicar migraciones (crea db.sqlite3)
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

▶️ Ejecutar el Proyecto
python manage.py runserver


La aplicación estará disponible en:
http://127.0.0.1:8000/
