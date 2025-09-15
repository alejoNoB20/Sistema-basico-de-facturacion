from models.db import db


class Producto(db.Model):
    __tablename__ = "producto"

    def __init__(self, descripcion, precio, stock):
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    id_producto = db.Column(db.Integer(), primary_key=True, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float(), nullable=False)
    stock = db.Column(db.Integer(), nullable=False)
    detalles = db.relationship("DetalleFactura", backref="producto")

    def actualizarProducto(self, descripcion, precio, stock):
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
