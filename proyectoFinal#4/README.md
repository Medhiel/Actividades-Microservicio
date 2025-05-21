# Administrador de Eventos - Microservicio Flask

Este proyecto es un microservicio desarrollado en **Flask** para la gestión de eventos, usuarios y roles. Permite el registro, autenticación y administración de eventos, con control de acceso por roles (Admin, Organizador, Participante).

## Características

- Registro e inicio de sesión de usuarios
- Gestión de roles (Admin, Organizador, Participante)
- CRUD de eventos (crear, editar, eliminar, listar)
- Protección de rutas con autenticación (`Flask-Login`)
- Formularios seguros con `Flask-WTF`
- Persistencia de datos con `Flask-SQLAlchemy` y MySQL
- Migraciones de base de datos con `Flask-Migrate`

## Requisitos

- Python 3.8+
- MySQL
- pip

## Instalación

1. **Clona el repositorio**
   ```sh
   git clone <URL-del-repo>
   cd <nombre-del-repo>
   ```

2. **Crea un entorno virtual (opcional pero recomendado)**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```

3. **Instala las dependencias**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**

   - Crea la base de datos ejecutando el script SQL:
     ```sh
     mysql -u <usuario> -p < 04_eventos.sql
     ```
   - Ajusta los datos de conexión en `config.py` si es necesario.

5. **Realiza las migraciones**
   ```sh
   flask db upgrade
   ```

6. **Crea usuarios y roles de prueba**
   ```sh
   python create_demo_users.py
   ```

7. **Ejecuta la aplicación**
   ```sh
   python run.py
   ```

8. **Accede en tu navegador**
   ```
   http://localhost:5000
   ```

## Estructura del Proyecto

```
📦 raiz_del_proyecto/
├── run.py                 # Punto de entrada de la app Flask
├── config.py              # Configuración global (clave secreta,DB URI)
├── requirements.txt       # Dependencias del proyecto
├── create_demo_users.py   # Script para crear usuarios iniciales (admin, participante, organizador)
├── README.md              # Documentación del proyecto
├── proyecto.pdf           # Documentación del proyecto requerida para entregar en el curso.
|
├── 📁 pruebas/            # Incluir todos los archivos necesarios para probar el CRUD principal
│   ├── create.rest             # Test file to Create a Row
│   ├── read.rest               # Test file to Read Rows
│   ├── read-a-row.rest         # Test file to Read only one Row
│   ├── update.rest             # Test file to Update a Row
│   ├── delete.rest             # Test file to Delete a Row
|
├── 📁 app/
│   ├── __init__.py             # Inicializa Flask, SQLAlchemy y Blueprints
│   ├── models.py               # Modelos de base de datos (User, Role, Evento)
│   ├── forms.py                # Formularios Flask-WTF (registro, login, evento, contraseña)
│   ├── routes.py               # Rutas protegidas (dashboard, eventos, cambiar contraseña)
│   ├── test_routes.py          # Rutas o end-points para pruebas (eventos)
│   ├── auth_routes.py          # Rutas públicas (login, registro, logout)
|   |
│   ├── 📁 templates/
│   │   ├── layout.html           # Plantilla base para todas las vistas
│   │   ├── index.html            # Página de bienvenida pública
│   │   ├── login.html            # Formulario de inicio de sesión
│   │   ├── register.html         # Formulario de registro con selector de rol
│   │   ├── dashboard.html        # Vista principal del usuario logueado
│   │   ├── evento_form.html      # Formulario para crear/editar eventos
│   │   ├── cursos.html           # Lista de eventos creados
│   │   ├── usuarios.html         # Vista de administración de usuarios (solo admin)
│   │   └── cambiar_password.html # Formulario para cambiar contraseña
|   |
│   └── 📁 static/
│       └── 📁 css/
│           └── styles.css              # (Opcional) Estilos personalizados
```

## Usuarios de Prueba

- **Admin**
  - Email: `admin@example.com`
  - Contraseña: `admin123`
- **Organizador**
  - Email: `organizador@example.com`
  - Contraseña: `organizador123`
- **Participante**
  - Email: `parti@example.com`
  - Contraseña: `parti123`

## Notas

- Para producción, recuerda cambiar la `SECRET_KEY` y desactivar el modo debug.
- Si necesitas restablecer la base de datos, ejecuta de nuevo el script SQL y el script de usuarios demo.

## Licencia

MIT

---

**Desarrollado por:**  
Adrian M. López Pino / R00652249