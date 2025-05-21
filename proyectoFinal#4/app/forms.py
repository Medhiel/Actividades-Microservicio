from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Formulario para login de usuario
class LoginForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

# Formulario para registrar un nuevo usuario
class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Rol', choices=[('Participante', 'Participante'), ('Organizador', 'Organizador'), ('Admin', 'Admin')], validators=[DataRequired()])
    submit = SubmitField('Registrarse')

# Formulario para cambiar la contraseña del usuario
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm new password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update Password')

# Formulario para crear o editar un curso
class EventoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=150)])
    ubicacion = StringField('Ubicación', validators=[DataRequired(), Length(max=200)])
    fecha_hora = DateTimeField('Fecha y Hora', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    capacidad = IntegerField('Capacidad', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    submit = SubmitField('Guardar')