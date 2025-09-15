from models.db import db


class Cliente(db.Model):
    __tablename__ = "cliente"

    def __init__(self, nombre, direccion, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    id_cliente = db.Column(db.Integer(), primary_key=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.Integer(), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    factura = db.relationship("Factura", backref="cliente", lazy=True)

    def actualizarCliente(self, nombre, direccion, telefono, email) -> bool:
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        return True
