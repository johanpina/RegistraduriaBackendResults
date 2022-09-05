from Modelos.Mesa import Mesa

class ControladorMesa():

    def __init__(self):
        print("Creando una Mesa")
    def index(self):
        print('listar todas las mesas')
        mesa={
            "Numero": 1,
            "Ubicacion": "Colegio Sagrado Corazon",
            "Cantidad": 100

        }
        mesa2 = {
            "Numero": 2,
            "Ubicacion": "Normal superior santa Teresita",
            "Cantidad": 450
        }
        return[mesa,mesa2]

    def create(self, infoMesa):
        print('Crear una Mesa')
        laMesa = Mesa(infoMesa)
        return {"mensaje": "Mesa creada Satisfactoriamente", "Mesa": laMesa.__dict__}

    def show(self, numero):
        print('Mostrando una mesacon Numero: ', numero)
        unamesa = {
            "Numero": 1,
            "Ubicacion": "Colegio Sagrado Corazon",
            "Cantidad": 100

        }
        return unamesa

    def update(self,numero,infoMesa):
        print("Actualizando Mesa con Numero: ", numero)
        laMesa= Mesa(infoMesa)
        return {"mensaje": "Mesa actualizada Satisfactoriamente", "mesa": laMesa.__dict__}

    def delete(self, numero):
        print("Eliminando Mesa con numero ", numero)
        return {"mensaje": "Mesa eliminada correctamente"}