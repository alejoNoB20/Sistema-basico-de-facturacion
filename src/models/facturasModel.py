from models.db import db


class Factura(db.Model):
    __tablename__ = "factura"

    def __init__(self, id_cliente, fecha, total):
        self.id_cliente = id_cliente
        self.fecha = fecha
        self.total = total

    id_factura = db.Column(db.Integer(), primary_key=True, nullable=False)
    id_cliente = db.Column(
        db.Integer(), db.ForeignKey("cliente.id_cliente"), nullable=False
    )
    fecha = db.Column(db.Date(), nullable=True)
    total = db.Column(db.Numeric(), nullable=False)
    detalles = db.relationship("DetalleFactura", backref="factura")
