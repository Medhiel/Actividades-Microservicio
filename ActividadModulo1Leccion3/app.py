from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para almacenar usuarios
usuarios = []

# Ruta GET /info
@app.route("/info", methods=["GET"])
def get_info():
    info = {
        "nombre_sistema": "Sistema de Usuarios",
        "version": "1.0",
        "descripcion": "API que permite crear y listar usuarios."
    }
    return jsonify(info), 200

# Ruta POST /crearUsuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400

    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or not correo:
        return jsonify({"error": "Se requieren los campos 'nombre' y 'correo'"}), 400

    nuevo_usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(nuevo_usuario)

    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": nuevo_usuario
    }), 201

# Ruta GET /usuarios
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios}), 200

if __name__ == "__main__":
    app.run(debug=True)
