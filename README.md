# Libreria
Este proyecto Django es una aplicación web para gestionar una librería virtual. Proporciona funciones para mostrar libros, agregar nuevos libros, editar la información existente y eliminar libros. La aplicación está diseñada utilizando el framework Django de Python intentando seguir las mejores practicas.

## Características Principales
- **Visualización de Libros:** Interfaz para ver todos los libros disponibles en la librería.
- **Creación de Libros:** Formulario para agregar nuevos libros a la colección.
- **Edición de Información:**  Capacidad para editar detalles como título, descripción e imagen de un libro.
- **Eliminación de Libros:** Funcionalidad para eliminar libros de la base de datos.
- **Gestión de Imágenes:** El proyecto incluye una función para eliminar las imágenes asociadas a un libro cuando se elimina el libro.

## Estructura del Proyecto

- **Libreria:** Contiene los archivos relacionados con la aplicación de la Librería.
- **Sistema:** Contiene archivos de configuración y ajustes del proyecto Django.
- **manage.py:** Archivo principal para gestionar el proyecto Django.
- **README.md:** Instrucciones detalladas sobre cómo configurar y ejecutar el proyecto.

## Estructura del Proyecto "Sistema"

- **__init__.py:** Archivo de inicialización.
- **asgi.py:** Configuración para ASGI (Asynchronous Server Gateway Interface).
- **settings.py:** Configuración principal del proyecto Django.
- **urls.py:** Configuración de las URL del proyecto.
- **wsgi.py:** Configuración para WSGI (Web Server Gateway Interface).

  ## Estructura de la Aplicación "Libreria"

- **admin.py:** Configuración del panel de administración.
- **apps.py:** Configuración de la aplicación.
- **forms.py:** Definición de formularios.
- **migrations/:** Archivos de migración de la base de datos.
- **models.py:** Definición de modelos.
- **tests.py:** Archivos de pruebas.
- **urls.py:** Configuración de las URL de la aplicación.
- **views.py:** Lógica de las vistas.


## Configuración del Entorno

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/Ionutpascariu/Libreria.git
    ```

2. **Crea un entorno virtual e instala las dependencias:**
    ```bash
    cd Libreria
    python -m venv venv
    source venv/bin/activate   # o `venv\Scripts\activate` en Windows
    pip install -r requirements.txt
    ```

3. **Realiza las migraciones:**
    ```bash
    python manage.py migrate
    ```

4. **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```


## Contribuciones

¡Contribuciones son bienvenidas! Si deseas contribuir, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama: `git checkout -b feature/nueva-caracteristica`.
3. Realiza tus cambios y haz commit: `git commit -m 'Agrega nueva característica'`.
4. Haz un push a la rama: `git push origin feature/nueva-caracteristica`.
5. Abre un pull request.


