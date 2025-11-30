# 🐾 HUELLAS FELICES - Plataforma de Adopción (Proyecto Semestral)

## 🌟 Descripción del Proyecto

**Huellas Felices** es una plataforma web desarrollada en **Django** que sirve como punto de encuentro digital para la adopción responsable de perros y gatos.

El proyecto simula la funcionalidad de sitios de adopción reales, permitiendo a los rescatistas y refugios publicar fichas detalladas de las mascotas, mientras que los usuarios pueden buscar, filtrar y solicitar la adopción de un animal.

Este repositorio documenta el desarrollo completo del sistema, incluyendo la estructura de la base de datos (modelos), la lógica de la aplicación (vistas), y la presentación visual (plantillas).

## 💡 Objetivos del Proyecto (Parcial/Semestral)

El desarrollo de Huellas Felices tiene como fin demostrar la competencia en los siguientes temas clave de la asignatura:

1.  **Dominio del Framework Django:** Utilización de Modelos, Vistas Basadas en Clases (CBV) y el sistema de plantillas.
2.  **Modelado de Datos:** Diseño de una Base de Datos relacional (`Mascota`, `Usuario`, `Solicitud de Adopción`).
3.  **CRUD y Formularios:** Implementación de las operaciones básicas (Crear, Leer, Actualizar, Borrar) para el manejo de las mascotas.
4.  **Autenticación y Permisos:** Gestión de usuarios (Adoptantes vs. Rescatistas) y restricción de acceso a ciertas funcionalidades.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.13.7, **Django 5.2.8**
* **Base de Datos:** SQLite3 (Desarrollo)
* **Manejo de Archivos/Imágenes:** **Pillow**
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap

---

## 🚀 Guía de Instalación y Ejecución

Sigue estos pasos para levantar el proyecto en tu entorno local.

### 1. Clonar el Repositorio

Abre tu terminal (Git Bash) y ejecuta:

```bash
git clone [https://github.com/yohangaitan/huellas-felices.git](https://github.com/yohangaitan/huellas-felices.git)
cd huellas-felices

2. Configurar el Entorno Virtual
Bash

# Crear entorno virtual
python -m venv venv
# Activar el entorno (Usa el comando apropiado para tu sistema)
# Windows (Git Bash/MingW):
source venv/Scripts/activate
# Linux/macOS:
# source venv/bin/activate
3. Instalar Dependencias
¡Paso Crítico! Crea un archivo llamado requirements.txt en la raíz de tu proyecto y añade el siguiente contenido:

Plaintext

Django>=5.0
Pillow>=10.0
Luego, instala las dependencias:

Bash

pip install -r requirements.txt
4. Configurar la Base de Datos
Bash

# Crear el archivo de migración para la aplicación 'mascotas'
python manage.py makemigrations mascotas
# Aplicar todas las migraciones (crea la base de datos SQLite)
python manage.py migrate
5. Crear Superusuario (Acceso al Admin)
Bash

python manage.py createsuperuser
6. Ejecutar el Servidor
Bash

python manage.py runserver
Accede a http://127.0.0.1:8000/ para ver la aplicación.
