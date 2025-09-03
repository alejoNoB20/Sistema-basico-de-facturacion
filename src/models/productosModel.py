from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    __tablename__ = "prodcuto"

    def __init__ (self, id_producto, descripcion, precio, stock):
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    id_usuario = db.Column(db.Integer, primary_key=True, allownull=False)
    nombre = db.Column(db.String(50), allownull=False)
    email = db.Column(db.String(100), allownull=True)
    password = db.Column(db.string(50), allownull=False)
    rol = db.Column(db.String(50), allownull=False)

