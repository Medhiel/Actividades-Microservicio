from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Página principal con formulario de registro
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", error=None)

# Página de registro para procesar el formulario
@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            error = "Username is required."
        else:
            message = f"User {username} registered successfully!"
            return render_template("home.html", message=message)
        
    return render_template("index.html", error=error)

# Página de productos (simple lista de ejemplo)
@app.route("/productos")
def productos():
    productos = ["Producto 1", "Producto 2", "Producto 3"]
    return render_template("productos.html", productos=productos)

# Página de usuarios (tabla de ejemplo)
@app.route("/usuarios")
def usuarios():
    usuarios = [
        {"nombre": "Juan", "email": "juan@email.com"},
        {"nombre": "Ana", "email": "ana@email.com"},
        {"nombre": "Luis", "email": "luis@email.com"}
    ]
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
