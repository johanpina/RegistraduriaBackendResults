from Modelos.Partido import Partido

class ControladorPartido():

    def __init__(self):
        print('creando un partido')

    def index(self):
        print('Listar todos los partidos')
        unPartido = {
            "nombre": "Pacto historico",
            "lema": "Queremos paz total"
        }
        otroPartido = {
            "nombre": "Centro democrático",
            "lema": "Mano firme corazón grande"
        }

        return  [unPartido, otroPartido]

    def create(self, infoPartido):
        print('Crear un partido')
        elPartido = Partido(infoPartido)
        return {"mensaje": "Partido creado Satisfactoriamente", "partido":elPartido.__dict__}


    def show(self, id):
        print('Mostrando un partido con id: ',id)
        unPartido = {
            "id": 1,
            "nombre": "Pacto historico",
            "lema": "Queremos paz total"
        }
        return unPartido


    def update(self, id, infoPartido):
        print("Actualizando partido con id: ",id)
        elPartido = Partido(infoPartido)
        return {"mensaje": "Partido actualizado Satisfactoriamente", "partido": elPartido.__dict__}

    def delete(self, id):
        print("Eliminando Partido con id ", id)
        return {"mensaje": "Partido eliminado Correctamente"}