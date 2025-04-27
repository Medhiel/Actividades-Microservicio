from flask import Flask, render_template, redirect, url_for, request, flash
from flask_principal import Principal, Permission, RoleNeed
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Configuración de la app Flask
app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # Cambia esto por una clave secreta real
principal = Principal(app)

# Configuración de Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login_page"

# Definición de roles utilizando Flask-Principal
admin_role = RoleNeed('admin')
user_role = RoleNeed('user')

# Definición de permisos asociados a roles
admin_permission = Permission(admin_role)
user_permission = Permission(user_role)

# Simulando una base de datos de usuarios
class User(UserMixin):
    def __init__(self, id, role):
        self.id = id
        self.role = role

# Diccionario con usuarios simulados
users = {
    'admin': User('admin', 'admin'),
    'user': User('user', 'user')
}

# Función para cargar un usuario por su ID
@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Ruta principal
@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('protected_page'))
    return redirect(url_for('login_page'))

# Página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        role = request.form['role']
        user = users.get(username)
        
        if user and user.role == role:
            login_user(user)
            flash('Has iniciado sesión correctamente', 'success')  # Mensaje de inicio de sesión exitoso
            return redirect(url_for('protected_page'))
        else:
            flash('Credenciales inválidas', 'error')  # Mensaje de error si las credenciales son incorrectas
            return redirect(url_for('login_page'))
    
    return render_template('login.html')

# Página protegida (solo accesible para usuarios autenticados)
@app.route('/protected')
@login_required
def protected_page():
    if current_user.role == 'admin':
        return f'Bienvenido {current_user.id}, acceso autorizado como admin.'
    elif current_user.role == 'user':
        return f'Bienvenido {current_user.id}, acceso autorizado como usuario.'
    else:
        return redirect(url_for('home'))

# Ruta para cerrar sesión
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Cierra la sesión
    flash('Has sido desconectado correctamente', 'info')  # Muestra un mensaje de confirmación
    return redirect(url_for('login_page'))  # Redirige a la página de inicio de sesión

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
