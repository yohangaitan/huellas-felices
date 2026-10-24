# 🏡 Huellas Felices: Plataforma de Adopción de Mascotas

Huellas Felices es una aplicación web desarrollada con Django que digitaliza el proceso de publicación y adopción de perros y gatos en Panamá. Conecta de forma simple a quienes buscan un nuevo compañero con quienes necesitan encontrarle un hogar seguro a un animal.

## ✨ Características

- **Cuentas de usuario:** registro, inicio de sesión y gestión de las propias publicaciones y del perfil.
- **Publicación detallada:** especie, raza, género, edad, tamaño, color, provincia (las 10 provincias y las 3 comarcas), descripción y foto.
- **Listados con filtros:** perros y gatos por separado, búsqueda por texto y filtros por tamaño, edad, género, color y provincia, con paginación que conserva los filtros.
- **Contacto directo:** botón de WhatsApp hacia quien publica la mascota (solo mientras esté disponible).
- **Estados de adopción:** desde *Mis publicaciones* el dueño marca cada mascota como Disponible, En proceso o Adoptado.
- **Blog:** artículos educativos sobre adopción y cuidado, administrables desde el panel de Django.
- **Datos de demostración versionados:** mascotas, artículos e imágenes viajan con el repo (ver [más abajo](#-datos-de-demostración)).

## 💻 Tecnologías

| Categoría | Tecnología |
|---|---|
| Backend | Python 3.11+, Django 5.2 |
| Frontend | Plantillas de Django, Tailwind CSS (CDN), Bootstrap Icons |
| Base de datos | SQLite por defecto; PostgreSQL con la variable `DATABASE_URL` |
| Producción | Gunicorn, WhiteNoise, dj-database-url |

## 🚀 Inicio rápido

Requisitos: Python 3.11 o superior y Git.

```bash
git clone https://github.com/yohangaitan/huellas-felices.git
cd huellas-felices

# Entorno virtual
python -m venv venv
source venv/bin/activate        # macOS / Linux
.\venv\Scripts\Activate         # Windows (PowerShell)

pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_demo    # ← carga las mascotas y los artículos de ejemplo
python manage.py runserver
```

Abre <http://127.0.0.1:8000/>. Para entrar al panel de administración crea un superusuario con `python manage.py createsuperuser` y visita `/admin/`.

> **Si el sitio aparece vacío**, falta ejecutar `python manage.py cargar_demo`. La base de datos (`db.sqlite3`) y las fotos subidas (`media/`) no se guardan en git: son datos de cada instalación.

## 📦 Datos de demostración

El contenido de ejemplo vive en [`datos_demo/`](datos_demo/):

```
datos_demo/
├── mascotas.json
├── articulos.json
└── media/            # fotos de las mascotas y portadas del blog
```

Dos comandos lo mueven en cada dirección:

| Comando | Dirección | Para qué |
|---|---|---|
| `cargar_demo` | repo → tu base de datos | Que un clon o un servidor nuevo tenga contenido. |
| `exportar_demo` | tu base de datos → repo | Que lo que publiques tú viaje al repo. |

### Cargar (`cargar_demo`)

Es **idempotente**: solo crea lo que falta y nunca sobrescribe lo que hayas editado, así que puedes ejecutarlo las veces que quieras.

```bash
python manage.py cargar_demo --usuario mi_usuario --whatsapp 50760000000
```

| Opción | Para qué sirve |
|---|---|
| `--usuario` | Usuario que figurará como publicador de las mascotas (por defecto `huellas_demo`, una cuenta sin contraseña). Usa tu propio usuario si quieres editarlas desde el sitio. |
| `--whatsapp` | Número con código de país y solo dígitos. Sin él, las fichas no muestran el botón de WhatsApp. |
| `--origen` | Carpeta de la que leer los datos (por defecto `datos_demo/`). |

### Publicar tus propias mascotas en el repo (`exportar_demo`)

1. Publica mascotas desde el sitio (o artículos desde `/admin/`) en tu entorno local.
2. Exporta:

   ```bash
   python manage.py exportar_demo --dry-run   # opcional: muestra qué haría, sin escribir
   python manage.py exportar_demo
   ```

3. Revisa y sube los cambios:

   ```bash
   git status                                  # debería mostrar solo cambios en datos_demo/
   git add datos_demo
   git commit -m "Actualizar datos de demo"
   git push
   ```

4. En el servidor: `git pull` y `python manage.py cargar_demo --usuario TU_USUARIO` (con el **mismo** usuario de siempre, para no duplicar).

| Opción | Para qué sirve |
|---|---|
| `--usuario` | Exporta solo las mascotas publicadas por ese usuario (por defecto, todas). Los artículos se exportan siempre. |
| `--dry-run` | Muestra el resultado sin escribir ni copiar nada. |
| `--limpiar` | Borra de `datos_demo/media/` las imágenes que ya no usa ningún registro. |
| `--forzar` | Permite exportar listas vacías. Sin esta opción el comando se niega, para que nadie borre los datos del repo desde un clon recién migrado. |
| `--destino` | Carpeta de salida (por defecto `datos_demo/`). |

**Qué se exporta y qué no.** Se exportan los datos de cada mascota y artículo con sus imágenes. No se exporta ningún dato de cuentas: ni usuarios, ni correos, ni contraseñas, ni teléfonos de WhatsApp.

**A tener en cuenta:**

- El repositorio es público: el comando avisa si una descripción parece contener un teléfono, pero revisa tú lo que subes.
- `cargar_demo` identifica cada mascota por su **nombre y su publicador**. Dos mascotas con el mismo nombre se cargarían como una sola (el exportador lo avisa), y editar una mascota que ya fue cargada no se propaga a las instalaciones que ya la tienen.
- Las fotos se versionan en git: conviene reducirlas antes de subirlas (unos cientos de KB bastan para una ficha).

## ⚙️ Variables de entorno

Sin ninguna variable el proyecto corre en modo desarrollo. En producción se configuran así:

| Variable | Descripción | Ejemplo |
|---|---|---|
| `DEBUG` | `0` en producción (por defecto `1`) | `0` |
| `SECRET_KEY` | Obligatoria si `DEBUG=0` | cadena larga y aleatoria |
| `ALLOWED_HOSTS` | Dominios permitidos, separados por comas | `usuario.pythonanywhere.com` |
| `CSRF_TRUSTED_ORIGINS` | Orígenes HTTPS confiables | `https://usuario.pythonanywhere.com` |
| `DATABASE_URL` | Opcional. Si existe se usa en lugar de SQLite | `postgresql://...` |
| `PROXY_SSL` | `1` si la plataforma sirve HTTPS tras un proxy | `1` |
| `SECURE_SSL_REDIRECT` | `1` para redirigir HTTP a HTTPS | `1` |
| `SERVE_MEDIA` | `1` para servir `/media/` desde Django (solo demos) | `1` |
| `EMAIL_BACKEND` | Por defecto imprime los correos en consola | `django.core.mail.backends.smtp.EmailBackend` |

Genera una `SECRET_KEY` con:

```bash
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
```

La `SECRET_KEY` nunca debe subirse a git. Si alguna vez estuvo en el repositorio, usa una nueva en producción.

## 🌐 Despliegue

La guía paso a paso para publicar el sitio gratis en PythonAnywhere (con base de datos y fotos persistentes) está en [DESPLIEGUE_PYTHONANYWHERE.md](DESPLIEGUE_PYTHONANYWHERE.md). Ten en cuenta que la cuenta gratuita vence a 1 mes y hay que extenderla desde la pestaña *Web*.

## 🧪 Pruebas

```bash
python manage.py test
```

La suite cubre paginación, cambio de estado, perfil, formularios, contacto por WhatsApp y los comandos `cargar_demo` y `exportar_demo`; entre ellos, una prueba de ida y vuelta que garantiza que exportar lo recién cargado reproduce exactamente `datos_demo/`.

## 🗂️ Estructura

```
huellasfelices/   configuración del proyecto (settings, urls, wsgi)
mascotas/         app principal: modelos, vistas, formularios, plantillas
  management/commands/   cargar_demo y exportar_demo
blog/             app del blog
datos_demo/       mascotas, artículos e imágenes de ejemplo
```
