# 🏡 Huellas Felices: Plataforma de Adopción de Mascotas

Huellas Felices es una aplicación web desarrollada con Django que digitaliza el proceso de publicación y adopción de mascotas. Su propósito es conectar de forma moderna y simple a quienes buscan un nuevo compañero peludo y a quienes necesitan encontrar un hogar seguro para sus animales.

## ✨ Características Clave del Proyecto

**Gestión de Usuarios:**  
Los usuarios pueden registrarse, iniciar sesión y administrar perfiles y publicaciones.

**Publicación Detallada:**  
Agregar tipo, tamaño, edad, provincia, descripción e imágenes.

**Listados Intuitivos:**  
Categorías de perros y gatos con páginas detalladas.

**Contacto Directo:**  
Enlaces para que adoptante y publicador se comuniquen.

**Blog Opcional:**  
Sección para contenido educativo sobre adopciones.

## 💻 Tecnologías Utilizadas

| Categoría     | Tecnología                      | Uso Principal                                                  |
|---------------|----------------------------------|----------------------------------------------------------------|
| Backend       | Python 3.x, Django 5.x           | Lógica, ORM, vistas, autenticación                            |
| Frontend      | HTML5, Tailwind CSS              | Diseño responsivo y estilización moderna                      |
| Base de Datos | SQLite3                          | Almacenamiento local y modelos                                |
| Estilos       | Bootstrap Icons, Widget Tweaks   | Iconos y formularios                                          |

## 🚀 Instalación y Puesta en Marcha

### 1. Requisitos

- Python 3.10+
- Git

### 2. Clonar el Repositorio

```bash
git clone https://github.com/yohangaitan/huellas-felices.git
cd huellas-felices
3. Crear Entorno Virtual
python -m venv venv

4. Activar Entorno Virtual

Windows

.\venv\Scripts\Activate


macOS / Linux

source venv/bin/activate

5. Instalar Dependencias
pip install -r requirements.txt

6. Migraciones y Superusuario
python manage.py migrate
python manage.py createsuperuser

▶️ Ejecutar el Proyecto
python manage.py runserver


La app estará activa en:
http://127.0.0.1:8000/
