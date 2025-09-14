from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = "usuario"

    def __init__(self, nombre, email, password, rol):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol

    id_usuario = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def crearHash(self):
        contraseñaConHash = generate_password_hash(self.password)
        self.password = contraseñaConHash
        return True

    def verificarContraseña(self, password):
        verificacion = check_password_hash(self.password, password)
        if not verificacion:
            return False
        return True
