from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import re

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Base de datos simulada
usuarios = {
    'admin': {'password': '12345', 'email': 'admin@example.com'},
    'adrian': {'password': '142414', 'email': 'adrian@example.com'}
}

# Clase de Usuario
class Usuario(UserMixin):
    def __init__(self, username):
        self.id = username

# Formulario de registro
class RegistrationForm(FlaskForm):
    nombre = StringField('Nombre de Usuario', 
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, message="El nombre debe tener al menos 3 caracteres.")
        ])
    correo = StringField('Correo Electrónico', 
        validators=[
            DataRequired(message="El correo es obligatorio."),
            Email(message="Ingrese un correo válido.")
        ])
    contraseña = PasswordField('Contraseña', 
        validators=[
            DataRequired(message="La contraseña es obligatoria."),
            Length(min=6, message="La contraseña debe tener al menos 6 caracteres.")
        ])
    submit = SubmitField('Registrarse')

# Cargar usuario desde la sesión
@login_manager.user_loader
def load_user(user_id):
    if user_id in usuarios:
        return Usuario(user_id)
    return None

# Ruta principal protegida
@app.route('/')
@login_required
def home():
    return render_template('home.html.jinja2', nombre=current_user.id)

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username]['password'] == password:
            user = Usuario(username)
            login_user(user)
            return redirect(url_for('home'))
        
        return render_template("error.html.jinja2", error_code=401, 
                               error_message="Invalid Credentials (error on username or password)!"), 401

    return render_template('login.html.jinja2') 

# Ruta de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.nombre.data
        email = form.correo.data
        password = form.contraseña.data

        if username in usuarios:
            flash('El nombre de usuario ya existe. Elija otro.', 'danger')
            return render_template('register.html.jinja2', form=form)

        # Simulamos guardar el usuario en "usuarios"
        usuarios[username] = {'password': password, 'email': email}
        flash('¡Registro exitoso! Ahora puede iniciar sesión.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html.jinja2', form=form)

# Ruta de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
