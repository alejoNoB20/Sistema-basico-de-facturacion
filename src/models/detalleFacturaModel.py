from models.db import db


class DetalleFactura(db.Model):
    __tablename__ = "detalle_factura"

    def __init__(self, id_factura, id_producto, cantidad, precio_unitario, subtotal):
        self.id_factura = id_factura
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal

    id_detalle = db.Column(db.Integer(), primary_key=True, nullable=False)
    id_factura = db.Column(
        db.Integer(), db.ForeignKey("factura.id_factura"), nullable=False
    )
    id_producto = db.Column(
        db.Integer(), db.ForeignKey("producto.id_producto"), nullable=False
    )
    cantidad = db.Column(db.Integer(), nullable=False)
    precio_unitario = db.Column(db.Float(), nullable=False)
    subtotal = db.Column(db.Float(), nullable=False)
