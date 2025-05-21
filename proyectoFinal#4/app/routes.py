from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user, login_user
from app.models import db, Evento, User, Role
from app.forms import EventoForm, ChangePasswordForm, LoginForm
from werkzeug.security import check_password_hash

eventos_bp = Blueprint('eventos', __name__)

@eventos_bp.route('/eventos')
@login_required
def listar_eventos():
    eventos = Evento.query.all()
    return render_template('dashboard.html', eventos=eventos)

@eventos_bp.route('/eventos/crear', methods=['GET', 'POST'])
@login_required
def crear_evento():
    form = EventoForm()
    if form.validate_on_submit():
        # lógica para crear el evento
        pass
    return render_template('eventos/form.html', form=form, titulo="Crear Evento")

@eventos_bp.route('/eventos/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_evento(id):
    evento = Evento.query.get_or_404(id)
    form = EventoForm(obj=evento)
    if form.validate_on_submit():
        evento.nombre = form.nombre.data
        evento.ubicacion = form.ubicacion.data
        evento.fecha_hora = form.fecha_hora.data
        evento.capacidad = form.capacidad.data
        evento.descripcion = form.descripcion.data
        db.session.commit()
        flash('Evento actualizado.', 'success')
        return redirect(url_for('eventos.listar_eventos'))
    return render_template('eventos/form.html', form=form, titulo='Editar Evento')

@eventos_bp.route('/eventos/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_evento(id):
    evento = Evento.query.get_or_404(id)
    db.session.delete(evento)
    db.session.commit()
    flash('Evento eliminado.', 'success')
    return redirect(url_for('eventos.listar_eventos'))

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/cambiar_password', methods=['GET', 'POST'])
@login_required
def cambiar_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        # lógica para cambiar la contraseña
        pass
    return render_template('cambiar_password.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html', form=form)


def check_password(self, password):
    return check_password_hash(self.password_hash, password)