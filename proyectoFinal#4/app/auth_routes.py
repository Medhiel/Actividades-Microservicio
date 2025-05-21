from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash

from app.forms import LoginForm, RegisterForm
from app.models import db, User, Role

# Blueprint de autenticación: gestiona login, registro y logout
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Inicia sesión de un usuario existente si las credenciales son válidas.
    """
    form = LoginForm()
    print("Método:", request.method)
    print("form.errors:", form.errors)

    # Procesamiento del formulario si es enviado correctamente
    if form.validate_on_submit():
        print("Formulario enviado")
        print("Email ingresado:", form.email.data)
        print("Password ingresado:", form.password.data)
        user = User.query.filter_by(email=form.email.data).first()
        print("Usuario encontrado:", user)

        # Verifica si el usuario existe y la contraseña es válida
        if user:
            print("Hash en BD:", user.password_hash)
            print("¿Contraseña correcta?:", user.check_password(form.password.data))
        if user and user.check_password(form.password.data):
            print("Contraseña correcta, login exitoso")
            login_user(user)
            return redirect(url_for('auth.login'))  # Cambia por una ruta que exista
        else:
            print("Credenciales inválidas")
            flash('Credenciales inválidas', 'danger')

    # Renderiza el formulario de login
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registra un nuevo usuario y lo asocia por defecto al rol "Student".
    """    
    form = RegisterForm()
    
    # Procesa el formulario si fue enviado correctamente
    if form.validate_on_submit():
        # Aquí sí puedes consultar la base de datos
        role = Role.query.filter_by(name=form.role.data).first()
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data),
            role_id=role.id
        )
        db.session.add(user)
        db.session.commit()
        flash('Usuario registrado exitosamente.', 'success')
        return redirect(url_for('auth.login'))
    
    # Renderiza el formulario de registro
    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    """
    Cierra sesión del usuario actual y redirige al login.
    """
    logout_user()
    return redirect('/')