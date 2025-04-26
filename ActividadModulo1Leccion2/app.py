from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bienvenido a mi API"


@app.route("/saludo", methods=["POST"])
def saludo():
    data = request.json
    nombre = data.get("nombre", "Usuario")
    return f"Hola, {nombre}!"


@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
    if request.method == "GET":
        return {"usuarios": ["Juan", "María", "Luis"]}
    if request.method == "POST":
        data = request.json
        nuevo_usuario = data.get("nombre")
        return {"mensaje": f"Usuario {nuevo_usuario} creado con éxito!"}, 201

if __name__ == "__main__":
    app.run(debug=True)