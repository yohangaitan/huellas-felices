# 🏡 Huellas Felices

Plataforma web de adopción de perros y gatos construida con Django, pensada para conectar a rescatistas y refugios con personas que quieren adoptar en Panamá. Proyecto académico.

## ✨ Características

- **Cuentas de usuario:** registro, inicio de sesión, recuperación de contraseña y perfil con número de WhatsApp.
- **Publicación de mascotas:** especie, raza, género, edad, tamaño, color, provincia, descripción y foto.
- **Listados con filtros:** perros y gatos por separado, búsqueda por texto, filtros por tamaño, edad, género, color y provincia, y paginación.
- **Contacto directo:** botón de WhatsApp hacia quien publica la mascota mientras esté disponible.
- **Gestión de publicaciones:** el dueño edita, elimina y marca cada mascota como Disponible, En proceso o Adoptada.
- **Blog:** artículos sobre adopción y cuidado de mascotas, administrables desde el panel de Django.

## 💻 Tecnologías

| Categoría | Tecnología |
|---|---|
| Backend | Python 3.11+, Django 5.2 |
| Frontend | Plantillas de Django, Tailwind CSS (CDN), Bootstrap Icons |
| Base de datos | SQLite (PostgreSQL opcional con `DATABASE_URL`) |
| Producción | Gunicorn, WhiteNoise |

## 🚀 Instalación

Requisitos: Python 3.11 o superior y Git.

```bash
git clone https://github.com/yohangaitan/huellas-felices.git
cd huellas-felices

python -m venv venv
source venv/bin/activate        # macOS / Linux
.\venv\Scripts\Activate         # Windows (PowerShell)

pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_demo    # mascotas y artículos de ejemplo
python manage.py runserver
```

Abre <http://127.0.0.1:8000/>. Para entrar al panel de administración (`/admin/`) crea un superusuario con `python manage.py createsuperuser`.

> Si el sitio aparece vacío, falta ejecutar `python manage.py cargar_demo`. La base de datos (`db.sqlite3`) y las fotos subidas (`media/`) no se guardan en git: son datos de cada instalación.

## 📦 Datos de demostración

Las mascotas, artículos e imágenes de ejemplo viven en `datos_demo/` y dos comandos los mueven entre el repo y tu base de datos local:

```bash
python manage.py cargar_demo      # repo → tu base de datos
python manage.py exportar_demo    # tu base de datos → repo
```

- **`cargar_demo`** crea lo que falta y no sobrescribe nada, así que se puede ejecutar cuantas veces haga falta. Opciones: `--usuario` (publicador de las mascotas; por defecto `huellas_demo`) y `--whatsapp` (número con código de país y solo dígitos, para que las fichas muestren el botón de contacto).
- **`exportar_demo`** copia a `datos_demo/` lo que hayas publicado en local. Después: `git add datos_demo && git commit -m "Actualizar datos de demo" && git push`. Opciones: `--usuario` (solo las mascotas de ese usuario), `--dry-run` (simula sin escribir) y `--limpiar` (borra imágenes sin uso). No exporta datos de cuentas (usuarios, correos, contraseñas ni teléfonos).

Ten en cuenta que el repositorio es público: revisa las descripciones antes de subirlas. Además, `cargar_demo` identifica cada mascota por su nombre y su publicador, y no actualiza las que ya existen.

## 🧪 Pruebas

```bash
python manage.py test
```

## 🌐 Despliegue

El proyecto incluye `Procfile` (Gunicorn), WhiteNoise para los archivos estáticos y configuración por variables de entorno. En el servidor define como mínimo:

| Variable | Valor |
|---|---|
| `DEBUG` | `0` |
| `SECRET_KEY` | una clave larga y aleatoria, nunca la subas a git |
| `ALLOWED_HOSTS` | tu dominio, p. ej. `miapp.example.com` |
| `CSRF_TRUSTED_ORIGINS` | tu dominio con esquema, p. ej. `https://miapp.example.com` |

Opcionales: `DATABASE_URL` (PostgreSQL), `PROXY_SSL`, `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`, `SERVE_MEDIA` y `EMAIL_BACKEND`. Una `SECRET_KEY` se genera con:

```bash
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
```

Luego, en el servidor:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py cargar_demo    # opcional
```

SQLite y `media/` necesitan un disco persistente; en plataformas con disco efímero se pierden en cada reinicio, y ahí hace falta PostgreSQL y almacenamiento externo para las fotos.

## 🗂️ Estructura

```
huellas-felices/
├── blog/                        # App del blog
│   ├── migrations/
│   ├── templates/blog/
│   └── admin.py, apps.py, models.py, tests.py, urls.py, views.py
├── datos_demo/                  # Mascotas, artículos e imágenes de ejemplo
├── huellasfelices/              # Configuración del proyecto
│   └── asgi.py, settings.py, urls.py, wsgi.py
├── mascotas/                    # App principal
│   ├── management/commands/     # cargar_demo.py y exportar_demo.py
│   ├── migrations/
│   ├── static/img/
│   ├── templates/               # mascotas/ (páginas y components/) y registration/
│   └── admin.py, apps.py, forms.py, models.py, signals.py, tests.py, urls.py, views.py
├── manage.py
├── Procfile
├── requirements.txt
└── runtime.txt
```

`media/`, `db.sqlite3` y el entorno virtual (`venv/` o `.venv/`) se generan en cada máquina y no se versionan.

## 👤 Autor

Hecho por [@yohangaitan](https://github.com/yohangaitan).
