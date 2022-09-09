from db import db

class Resultado2(db.Model):
    __tablename__ = "Resultados"

    id = db.Column(db.Integer(), primary_key=True)
    cantidad_votos = db.Column(db.Integer())
    id_candidato = db.Column(db.String(), db.ForeignKey('Candidato.cedula'))
    id_mesa = db.Column(db.String(), db.ForeignKey('Mesa.Numero'))

    def __init__(self, id, cantidad_votos, id_candidato, id_mesa):
        self.id = id
        self.cantidad_votos = cantidad_votos
        self.id_candidato = id_candidato
        self.id_mesa = id_mesa

    def __repr__(self):
        return f"Resultado id: {self.id}, Cantidad de votos: {self.cantidad_votos}, Id candidato: {self.id_candidato}, Id mesa: {self.id_mesa}"