from Modelos.Candidato2 import Candidato2
from db import db

class ControladorCandidato():

    def __init__(self):
        print("Creando ControladorCandidato")
        
    def index(self):
        get_candidato = []
        candidatos = Candidato2.query.all()
        for candidato in candidatos:
            result = {
                "cedula": candidato.cedula,
                "nombre": candidato.nombre,
                "apellido": candidato.apellido,
                "numero_res": candidato.numero_res,
                "correo": candidato.correo,
                "id_partido": candidato.partido_id
            }
            get_candidato.append(result)
        return get_candidato

        
    def create(self,data):
        candidato_cedula = data['cedula']
        candidato_nombre = data['nombre']
        candidato_apellido = data['apellido']
        candidato_numero_res = data['numero_res']
        candidato_correo = data['correo']
        candidato_partido = data['candidato_partido']
        elcandidato = Candidato2(candidato_cedula, candidato_nombre, candidato_apellido, candidato_numero_res, candidato_correo, candidato_partido)
        db.session.add(elcandidato)
        db.session.commit()
        respuesta = {
            "success": True,
            "response": "Candidato añadido"
        }
        return respuesta
        
    def show(self,cedula):
        candidato = Candidato2.query.get(cedula)
        result = {
            "cedula": candidato.cedula,
            "nombre": candidato.nombre,
            "apellido": candidato.apellido,
            "numero_res": candidato.numero_res,
            "correo": candidato.correo,
            "id_partido": candidato.partido_id
        }
        return result

    def update(self, cedula, data):
        candidato = Candidato2.query.get(cedula)
        candidato_nombre = data['nombre']
        candidato_apellido = data['apellido']
        candidato_numero_res = data['numero_res']
        candidato_correo = data['correo']
        candidato_partido = data['id_partido']
        if candidato is None:
            respuesta = {
                "success": False,
                "response": "No se encontró el candidato"
            }
        else:
            candidato.nombre = candidato_nombre
            candidato.apellido = candidato_apellido
            candidato.numero_res = candidato_numero_res
            candidato.correo = candidato_correo
            candidato.partido_id = candidato_partido
            db.session.merge(candidato)
            db.session.commit()
            respuesta = {
                "success": True,
                "response": "Candidato actualizado"
            }
        return respuesta

    def delete(self, cedula):
        candidato = Candidato2.query.get(cedula)
        if candidato is None:
            respuesta = {
                "success": False,
                "response": "No se encontró el candidato"
            }
        else:
            db.session.delete(candidato)
            db.session.commit()
            respuesta = {
                "success": True,
                "response": "Candidato eliminado"
            }
        return respuesta