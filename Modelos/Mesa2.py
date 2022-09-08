from main import db

class Mesa2(db.Model):
    __tablename__ = "Mesa"

    Numero = db.Column(db.String(), primary_key=True)
    Ubicacion = db.Column(db.String())
    Cantidad = db.Column(db.Integer())

    def __init__(self, Numero, Ubicacion, Cantidad):
        self.Numero = Numero
        self.Ubicacion = Ubicacion
        self.Cantidad = Cantidad


    def __repr__(self):
        return f"Numero de mesa : {self.Numero}, Ubicacion de la mesa: {self.Ubicacion}, Cantidad de sufragantes: {self.Cantidad}"
