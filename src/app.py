from flask import Flask, redirect, render_template, url_for, request
from models.usuariosModel import Usuario, db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.route("/crearDB")
def crearDB():
    db.create_all()
    return redirect(url_for("login"))


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        correo = request.form["email"]
        password = request.form["password"]
        usuario = db.session.query(Usuario).filter_by(email=correo).first()
        if not usuario:
            return render_template(
                "login.html", mensajeError="El mail ingreso no está registrado"
            )
        verificacionContraseña = usuario.verificarContraseña(password)
        if not verificacionContraseña:
            return render_template(
                "login.html", mensajeError="La contraseña ingresada es incorrecta"
            )
        return redirect(url_for("dashboard", id=usuario.id_usuario))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        nombre = request.form["name"]
        mail = request.form["email"]
        contraseña = request.form["password"]

        verificacionMail = db.session.query(Usuario).filter_by(email=mail).first()
        if verificacionMail:
            return render_template(
                "register.html", mensajeError="Ya existe una cuenta con el mismo mail"
            )
        else:
            nuevoUsuario = Usuario(nombre, mail, contraseña, "admin")
            nuevoUsuario.crearHash()
            db.session.add(nuevoUsuario)
            db.session.commit()
            return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    id = request.args.get("id", type=int)
    usuario = db.session.query(Usuario).filter_by(id_usuario=id).first()
    if not usuario:
        mensajeError = "Lo sentimos, no encontramos el usuario ingresado"
        return redirect(url_for("notFount404", mensaje=mensajeError))
    return render_template("dashboard.html", rol=usuario.rol)


@app.route("/notFount404")
def notFount404():
    mensaje = request.args.get("mensaje", type=str)
    return render_template("404.html", mensajeError=mensaje)


@app.route("/clients")
def clients():
    return render_template("clientes/verClientes.html")


@app.route("/products")
def products():
    return render_template("productos/verProductos.html")


@app.route("/invoices")
def invoices():
    return render_template("facturas/verFacturas.html")


if __name__ == "__main__":
    app.run(debug=True)
