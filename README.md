🏡 Huellas Felices: Plataforma de Adopción de Mascotas
Huellas Felices es una aplicación web completa desarrollada con Django que simplifica y digitaliza el proceso de publicación y adopción de mascotas. Nuestro objetivo es crear un puente intuitivo y moderno entre las personas que buscan un nuevo miembro peludo para su familia y los usuarios que necesitan encontrar un hogar seguro y amoroso para sus animales.

✨ Características Clave del Proyecto
Gestión de Usuarios y Perfiles: Los usuarios pueden registrarse y gestionar su información personal, así como sus publicaciones activas.

Publicación Detallada de Mascotas: Permite a los usuarios publicar mascotas especificando tipo (perro/gato), tamaño, edad, provincia, descripción, e imágenes.

Navegación Intuitiva: Listado separado por categorías (Perros y Gatos) y una página de detalle completa por cada mascota.

Integración de Contacto: Facilita la comunicación directa entre el interesado en adoptar y el publicador de la mascota a través de enlaces de contacto.

Blog de Contenido (Opcional): Incluye una sección de blog para compartir noticias, consejos de cuidado y concienciación sobre la adopción.

💻 Tecnologías Utilizadas
Categoría,Tecnología,Uso Principal
Backend,"Python 3.x, Django 5.x","Lógica de negocio, ORM, Vistas, Autenticación."
Frontend,"HTML5, Tailwind CSS","Estilización, diseño responsivo y componentes modernos."
Base de Datos,SQLite3 (Desarrollo),Almacenamiento local y gestión de modelos.
Estilos,"Bootstrap Icons, Widget Tweaks",Iconografía y renderizado de formularios.
🚀 Puesta en Marcha (Instalación Local)
Sigue estos pasos para descargar, configurar y ejecutar el proyecto en tu máquina local.

1. Requisitos Previos
Necesitas tener instalado lo siguiente:

Python 3.10 o superior

Git

2. Clonar el Repositorio
Abre tu terminal y descarga el código:
Bash

git clone https://github.com/tu-usuario/huellas-felices.git
cd huellas-felices
3. Configurar el Entorno
Es crucial crear y activar un entorno virtual (venv) para aislar las librerías del proyecto de las librerías globales de tu sistema.

Bash

# Crea el entorno virtual
python -m venv venv

# Activa el entorno virtual
# En Windows (PowerShell/CMD):
# .\venv\Scripts\Activate
# En macOS/Linux:
source venv/bin/activate
4. Instalación de Librerías
Una vez activado el entorno, se instalarán todas las dependencias de Python listadas en el archivo requirements.txt.

Librerías principales que se instalan:

Django: El framework web principal.

Pillow: Necesario para el manejo y procesamiento de imágenes.

django-widget-tweaks: Ayuda a estilizar los formularios de Django con Tailwind CSS.

Bash

pip install -r requirements.txt
5. Configurar la Base de Datos y Superusuario
Se utiliza SQLite, que se configura automáticamente. Solo necesitas aplicar las estructuras de la base de datos (migraciones).

Bash

# 1. Aplica las migraciones a la base de datos (crea el archivo db.sqlite3)
python manage.py migrate

# 2. Crea un usuario administrador para acceder al /admin/ (Opcional)
python manage.py createsuperuser
▶️ Ejecución del Proyecto
Para ver la aplicación en funcionamiento, inicia el servidor de desarrollo de Django:

Bash

python manage.py runserver
La aplicación estará disponible en tu navegador en: http://127.0.0.1:8000/
