from db import db

class Partido2(db.Model):
    __tablename__ = "Partido"

    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String())
    lema =  db.Column(db.String())
    candidato = db.relationship('Candidato2')

    def __init__(self, id, nombre, lema):
        self.id = id
        self.nombre = nombre
        self.lema = lema

    def __repr__(self):
        return f"id_partido : {self.id}, nombre: {self.nombre}, lema: {self.lema}"