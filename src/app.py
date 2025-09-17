from flask import Flask, redirect, render_template, url_for, request, session
from models.db import db
from models.usuariosModel import Usuario
from models.clientesModel import Cliente
from models.facturasModel import Factura
from models.productosModel import Producto


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = "contraseña_recontra_secreta_confia_en_mi"
db.init_app(app)


@app.route("/crearDB")
def crearDB():
    db.drop_all()
    db.create_all()
    admin = Usuario("admin", "admin@admin.com", "admin", "admin")
    admin.crearHash()
    db.session.add(admin)
    db.session.commit()
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
        session["id_usuario"] = usuario.id_usuario
        session["nombre_usuario"] = usuario.nombre
        session["rol_usuario"] = usuario.rol
        return redirect(url_for("dashboard"))


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
            nuevoUsuario = Usuario(nombre, mail, contraseña, "usuarioAutorizado")
            nuevoUsuario.crearHash()
            db.session.add(nuevoUsuario)
            db.session.commit()
            return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if not "id_usuario" in session:
        return redirect(url_for("notFount404", url="/", msg="Volver al inicio"))
    rol = session["rol_usuario"]
    return render_template("dashboard.html", rol=rol)


@app.route("/notFount404")
def notFount404():
    return render_template("404.html", url="/", msg="Volver al inicio")


@app.route("/clients")
def clients():
    clientes = db.session.query(Cliente).all()
    print(clientes)
    return render_template("clientes/verClientes.html", clientes=clientes)


@app.route("/clients/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("clientes/crearCliente.html")
    else:
        nombre = request.form["nombre"]
        direccion = request.form["direccion"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        cliente = Cliente(nombre, direccion, telefono, email)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for("clients"))


@app.route("/clients/delete/<int:id>")
def delete(id):
    cliente = db.session.query(Cliente).filter(Cliente.id_cliente == id)
    if not cliente:
        return redirect(
            url_for("notFount404", url="clients", msg="Volver a la lista de clientes")
        )
    cliente.delete(synchronize_session="auto")
    db.session.commit()
    return redirect(url_for("clients"))


@app.route("/clients/update/<int:id>", methods=("GET", "POST"))
def update(id):
    cliente = db.session.query(Cliente).filter(Cliente.id_cliente == id).first()
    if not cliente:
        return redirect(
            url_for("notFount404", url="clients", msg="Volver a la lista de clientes")
        )
    if request.method == "GET":
        return render_template("clientes/actualizarClientes.html", cliente=cliente)
    else:
        nombre = request.form["nombre"]
        direccion = request.form["direccion"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        cliente.actualizarCliente(nombre, direccion, telefono, email)
        db.session.commit()
        return redirect(url_for("clients"))


@app.route("/products")
def products():
    productos = db.session.query(Producto).all()
    return render_template("productos/verProductos.html", productos=productos)


@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("productos/crearProducto.html")
    else:
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        producto = Producto(descripcion, precio, stock)
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for("products"))


@app.route("/products/delete/<int:id>")
def delete_product(id):
    producto = db.session.query(Producto).filter(Producto.id_producto == id)
    if not producto:
        return redirect(
            url_for("notFount404", url="products", msg="Volver a lista de Productos")
        )
    producto.delete(synchronize_session="auto")
    db.session.commit()
    return redirect(url_for("products"))


@app.route("/product/update/<int:id>", methods=["GET", "POST"])
def update_product(id):
    producto = db.session.query(Producto).filter(Producto.id_producto == id).first()
    if not producto:
        return redirect(
            url_for("notFount404", url="products", msg="Volver a lista de Productos")
        )
    if request.method == "GET":
        return render_template("productos/actualizarProducto.html", producto=producto)
    else:
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        stock = request.form["stock"]
        producto.actualizarProducto(descripcion, precio, stock)
        db.session.commit()
        return redirect(url_for("products"))


@app.route("/invoices")
def invoices():
    return render_template("facturas/verFacturas.html")


@app.route("/invoice/add")
def add_invoice():
    print("ENTRA ACA")
    clientes = db.session.query(Cliente).all()
    productos = db.session.query(Producto).all()
    return render_template(
        "facturas/emitirFactura.html",
        clientes=clientes,
        productos=productos,
    )


@app.route("/invoices/add_product")
def add_invoice_product():
    lista = []
    producto = request.form["producto"]
    cantidad = request.form["cantidad"]
    lista.append({producto: producto, cantidad: cantidad})
    clientes = db.session.query(Cliente).all()
    productos = db.session.query(Producto).all()
    return render_template(
        "facturas/emitirFactura.html",
        clientes=clientes,
        productos=productos,
        lista=lista,
    )


@app.route("/invoices/create")
def create_invoice():
    return redirect(url_for("invoices"))


@app.route("/invoices/details/<int:id>")
def details_invoices(id):
    return render_template("facturas/detalleFactura.html")


if __name__ == "__main__":
    app.run(debug=True)
