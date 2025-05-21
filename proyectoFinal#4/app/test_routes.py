from flask import Blueprint, request, jsonify, render_template
from app.models import db, Curso, Evento
from app.forms import EventoForm
from flask_login import login_required

# Blueprint solo con endpoints de prueba para cursos
main = Blueprint('main', __name__)

@main.route('/') # Ambas rutas llevan al mismo lugar
@main.route('/dashboard')
def index():
    """
    Página de inicio pública (home).
    """
    return '<h1>Corriendo en Modo de Prueba.</h1>'

@main.route('/eventos', methods=['GET'])
def listar_eventos():
    """
    Retorna una lista de eventos (JSON).
    """
    eventos = Evento.query.all()

    data = [
        {'id': evento.id, 'titulo': evento.titulo, 'descripcion': evento.descripcion, 'profesor_id': evento  .profesor_id}
        for evento in eventos
    ]
    return jsonify(data), 200


@main.route('/eventos/<int:id>', methods=['GET'])
def listar_un_evento(id):
    """
    Retorna un solo evento por su ID (JSON).
    """
    evento = Evento.query.get_or_404(id)

    data = {
        'id': evento.id,
        'titulo': evento.titulo,
        'descripcion': evento.descripcion,
        'profesor_id': evento.profesor_id
    }

    return jsonify(data), 200


@main.route('/eventos', methods=['POST'])
def crear_evento():
    """
    Crea un evento sin validación.
    Espera JSON con 'titulo', 'descripcion' y 'organizador_id'.
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    evento = Evento(
        titulo=data.get('titulo'),
        descripcion=data.get('descripcion'),
        organizador_id=data.get('organizador_id')  # sin validación de usuario
    )

    db.session.add(evento)
    db.session.commit()

    return jsonify({'message': 'Evento creado', 'id': evento.id, 'profesor_id': evento.profesor_id}), 201

@main.route('/cursos/<int:id>', methods=['PUT'])
def actualizar_curso(id):
    """
    Actualiza un curso sin validación de usuario o permisos.
    """
    evento = Evento.query.get_or_404(id)
    data = request.get_json()

    evento.titulo = data.get('titulo', evento.titulo)
    evento.descripcion = data.get('descripcion', evento.descripcion)
    evento.profesor_id = data.get('profesor_id', evento.profesor_id)

    db.session.commit()

    return jsonify({'message': 'Evento actualizado', 'id': evento.id}), 200

@main.route('/eventos/<int:id>', methods=['DELETE'])
def eliminar_evento(id):
    """
    Elimina un evento sin validación de permisos.
    """
    evento = Evento.query.get_or_404(id)
    db.session.delete(evento)
    db.session.commit()

    return jsonify({'message': 'Evento eliminado', 'id': evento.id}), 200

@main.route('/eventos/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_evento(id):
    evento = Evento.query.get_or_404(id)
    form = EventoForm(obj=evento)
    if form.validate_on_submit():
        # ... lógica para editar evento ...
        pass
    return render_template('eventos/form.html', form=form, titulo='Editar Evento')