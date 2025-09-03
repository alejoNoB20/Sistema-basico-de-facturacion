from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = "usuario"

    def __init__ (self, id_usuario, nombre, email, password, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol

    id_usuario = db.Column(db.Integer, primary_key=True, allownull=False)
    nombre = db.Column(db.String(50), allownull=False)
    email = db.Column(db.String(100), allownull=True)
    password = db.Column(db.string(50), allownull=False)
    rol = db.Column(db.String(50), allownull=False)

