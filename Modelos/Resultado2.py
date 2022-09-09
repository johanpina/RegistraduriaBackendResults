from main import db

class Resultado2(db.Model):
    __tablaname__ = 'Resultados'

    id = db.column(db.Integer(), primary_key=True)
    cantidad_votos = db.column(db.Integer())
    #id_candidato = db.column(db.Integer(), db.ForeignKey('Candidato.cedula'))
    #id_mesa = db.column(db.Integer(), db.ForeignKey('Mesa.Numero'))

    def __init__(self, id, cantidad_votos):#, id_candidato, id_mesa):
        self.id = id
        self.cantidad_votos = cantidad_votos
        #self.id_candidato = id_candidato
        #self.id_mesa = id_mesa

    def __repr__(self):
        return f"Resultado id: {self.id}, Cantidad de votos: {self.cantidad_votos}, Id candidato:, Id mesa: "