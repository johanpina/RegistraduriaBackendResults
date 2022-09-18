from Modelos.Partido2 import Partido2
from db import db


class ControladorPartido():

    def __init__(self):
        print('creando un partido')

    def index(self):
        print('Listar todos los partidos')
        get_partido = []
        partidos = Partido2.query.all()
        for partido in partidos:
            result = {
                "id": partido.id,
                "nombre": partido.nombre,
                "lema": partido.lema,

            }
            get_partido.append(result)
        return get_partido

    def create(self, data):
        #partido_id = data['id']
        partido_nombre = data['nombre']
        partido_lema = data['lema']
        elpartido = Partido2(partido_nombre, partido_lema)
        db.session.add(elpartido)
        db.session.commit()
        respuesta = {
            "success": True,
            "response": "Partido creado satisfactoriamente "
        }
        return respuesta


    def show(self, id):
        partido = Partido2.query.get(id)
        result = {
            "id": partido.id,
            "nombre": partido.nombre,
            "lema": partido.lema,
        }
        return result


    def update(self, id, data):
        partido = Partido2.query.get(id)
        partido_nombre = data['nombre']
        partido_lema = data['lema']

        if partido is None:
            respuesta = {
                "success": False,
                "response": "No se encontró el partido"
            }
        else:
            partido.nombre = partido_nombre
            partido.lema = partido_lema
            db.session.merge(partido)
            db.session.commit()
            respuesta = {
                "success": True,
                "response": "Partido actualizado exitosamente"
            }
        return respuesta

    def delete(self, id):
        partido = Partido2.query.get(id)
        if partido is None:
            respuesta = {
                "success": False,
                "response": "No se encontró el partido"
            }
        else:
            db.session.delete(partido)
            db.session.commit()
            respuesta = {
                "success": True,
                "response": "Partido eliminado exitosamente"
            }
        return respuesta