# Taller
🛠️ Proyecto Django - Taller Mecánico

Este proyecto implementa un sistema de gestión para un taller mecánico, desarrollado con Django. Permite gestionar mecánicos, vehículos y procedimientos de mantenimiento/reparación.

📌 Requerimientos

La aplicación debe implementar los siguientes elementos:

Mecánico: nombre, contacto, especialidad.

Vehículo: patente (única), modelo, año, dueño.

Procedimiento: nombre, descripción, mecánico (FK), vehículo (FK).

⚙️ Funcionalidades

CRUD completo (Crear, Listar, Modificar y Eliminar) para cada entidad.

Acceso al Django Admin configurado para visualizar y gestionar datos.

Relaciones entre mecánicos, vehículos y procedimientos.

📂 Estructura del Proyecto
taller_mecanico/
│── manage.py
│── db.sqlite3
│── README.md
│
├── taller/                # Aplicación principal
│   ├── migrations/        # Migraciones de la BD
│   ├── templates/         # Plantillas HTML
│   │   ├── mecanico/
│   │   ├── vehiculo/
│   │   └── procedimiento/
│   ├── admin.py           # Configuración del panel Admin
│   ├── models.py          # Definición de modelos
│   ├── views.py           # Lógica de vistas (CRUD)
│   ├── urls.py            # Rutas de la app
│   └── forms.py           # Formularios
│
└── taller_mecanico/       # Configuración del proyecto
    ├── settings.py
    ├── urls.py
    └── wsgi.py

🚀 Instalación y Uso

Clonar el repositorio

git clone https://github.com/usuario/taller_mecanico.git
cd taller_mecanico


Crear entorno virtual e instalar dependencias

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
pip install django


Aplicar migraciones

python manage.py makemigrations
python manage.py migrate


Crear superusuario para Admin

python manage.py createsuperuser


Levantar el servidor

python manage.py runserver


Acceder a:

http://127.0.0.1:8000/
 → CRUD de entidades

http://127.0.0.1:8000/admin/
 → Django Admin

🛡️ Configuración del Admin

En admin.py los modelos se registraron con:

list_display → mostrar campos principales en las tablas.

search_fields → búsqueda rápida.

list_filter → filtros laterales.

🧪 Datos de Prueba

Ejemplo de uso en Django Admin:

Crear un Mecánico: Juan Pérez, contacto 999999999, especialidad en motores.

Crear un Vehículo: patente "ABCD12", modelo "Toyota Corolla", año 2015, dueño "Pedro Soto".

Crear un Procedimiento: “Cambio de Aceite”, asociado a Juan Pérez y al Toyota Corolla.
