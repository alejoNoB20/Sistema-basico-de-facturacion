from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Factura(db.Model):
    __tablename__ = "factura"

    def __init__ (self, id_factura, id_cliente, fecha, total):
        self.id_factura = id_factura
        self.id_cliente = id_cliente
        self.fecha = fecha
        self.total = total

    id_factura = db.Column(db.Integer, primary_key=True, allownull=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('usuario.id'), allownull=False)
    fecha = db.Column(db.Date, allownull=True)
    total = db.Column(db.Numeric, allownull=False)
