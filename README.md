# 🐾 Huellas Felices

Un sistema de gestión de mascotas en adopción desarrollado con Django y Tailwind CSS.

---

## 🚀 Funcionalidades Principales (Estado Actual)

Este proyecto implementa las funcionalidades base de un sitio de adopción, con un enfoque en la gestión segura por parte del publicador:

1.  **Publicación y Listado de Mascotas:** Creación, visualización y filtrado básico de mascotas.
2.  **Gestión Segura (CRUD):**
    * **Edición y Eliminación Segura:** Solo el usuario que publicó una mascota puede editarla o eliminarla (protegido con `UserPassesTestMixin`).
3.  **Gestión de Perfil:** Los usuarios pueden crear y editar su información de contacto (integración con el modelo `UserProfile`).
4.  **Sistema de Solicitudes:**
    * Los adoptantes pueden enviar formularios de interés por cada mascota.
    * Los publicadores tienen un panel de **"Solicitudes Recibidas"** que muestra los datos de contacto del adoptante.
    * **Notificaciones:** El menú de usuario muestra el conteo total de solicitudes pendientes (`Solicitudes (X)`).

---

## ⚙️ Configuración y Ejecución del Proyecto

Sigue estos pasos para descargar, configurar el entorno y ejecutar la aplicación web en tu máquina local.

### 1. Requisitos Previos

* **Python 3.8+** (Recomendado Python 3.10 o superior)
* **Git**

### 2. Clonar el Repositorio

Abre tu terminal y clona el proyecto:

```bash
git clone [https://github.com/yohangaitan/huellas-felices.git](https://github.com/yohangaitan/huellas-felices.git)
cd huellas-felices
3. Configurar el Entorno Virtual (Recomendado)
Crea un entorno virtual para aislar las dependencias del proyecto:

Bash

# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activar el entorno virtual (Linux/macOS o Git Bash)
source venv/bin/activate
(Verás (venv) al inicio de tu línea de comandos, indicando que está activo.)

4. Instalar Dependencias de Python
Instala todas las librerías de Django y paquetes de terceros necesarios, incluyendo django-widget-tweaks para el estilizado de formularios:

Bash

pip install -r requirements.txt 
# Si no tienes un requirements.txt, usa:
# pip install django pillow django-widget-tweaks
5. Configuración de Django
Aplica las migraciones iniciales para crear la estructura de la base de datos (SQLite por defecto):

Bash

python manage.py migrate
6. Crear Superusuario
Crea una cuenta de administrador para acceder al panel de gestión (/admin/):

Bash

python manage.py createsuperuser
(Sigue las instrucciones para ingresar un nombre de usuario, email y contraseña.)

7. Ejecutar el Servidor
Inicia el servidor de desarrollo de Django:

Bash

python manage.py runserver
El proyecto estará accesible en tu navegador en: http://127.0.0.1:8000/
