from models.db import db

from werkzeug.security import check_password_hash, generate_password_hash


class Usuario(db.Model):
    __tablename__ = "usuario"

    def __init__(self, nombre, email, password, rol):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol

    id_usuario = db.Column(db.Integer(), primary_key=True, nullable=False)
    nombre = db.Column(db.String())
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))
    rol = db.Column(db.String(50))

    def crearHash(self):
        self.password = generate_password_hash(self.password)
        return True

    def verificarContraseña(self, password):
        verificacion = check_password_hash(self.password, password)
        if not verificacion:
            return False
        return True
