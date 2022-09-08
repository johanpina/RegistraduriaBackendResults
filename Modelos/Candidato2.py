from main import db


class Candidato2(db.Model):
    __tablename__ = "Candidato"

    cedula = db.Column(db.String(), primary_key=True)
    nombre =  db.Column(db.String())
    apellido = db.Column(db.String())
    numero_res = db.Column(db.String())
    correo = db.Column(db.String())

    def __init__(self, cedula, nombre, apellido, numero_res, correo):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.numero_res = numero_res
        self.correo = correo

    def __repr__(self):
        return f"NumeroResolucion : {self.numero_res},Nombre: {self.nombre}, Apellido : {self.apellido}"