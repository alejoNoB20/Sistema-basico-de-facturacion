from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = "cliente"

    def __init__ (self, id_cliente, nombre, direccion, telefono, mail):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.direccion = telefono
        self.mail = mail

    id_cliente = db.Column(db.Integer, primary_key=True, allownull=False)
    nombre = db.Column(db.String(50), allownull=False)
    email = db.Column(db.String(100), allownull=True)
    password = db.Column(db.string(50), allownull=False)
    rol = db.Column(db.String(50), allownull=False)
    factura = db.relationship('factura', backref='usuario', lazy=True)

