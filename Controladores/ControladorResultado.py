from Modelos.Resultado2 import Resultado2
from db import db

class ControladorResultado():

    def __init__(self):
        print("Creando resultado")

    def index(self):
        get_resultado = []
        resultados = Resultado2.query.all()
        for resultado in resultados:
            result = {
                "id": resultado.id,
                "cantidad_votos": resultado.cantidad_votos,
                "id_candidato": resultado.id_candidato,
                "id_mesa": resultado.id_mesa
            }
            get_resultado.append(result)
        return get_resultado

    def create(self, data):
        resultado_id = data['id']
        resultado_votos = data['cantidad_votos']
        resultado_candidato = data['id_candidato']
        resultado_mesa = data['id_mesa']
        elresultado = Resultado2(resultado_id, resultado_votos, resultado_candidato, resultado_mesa)
        db.session.add(elresultado)
        db.session.commit()
        respuesta = {
            "success": True,
            "response": "Resultado creado satisfactoriamente "
        }
        return respuesta


    def show(self, id):
        resultado = Resultado2.query.get(id)
        result = {
            "id": resultado.id,
            "cantidad_votos": resultado.cantidad_votos,
            "id_candidato": resultado.id_candidato,
            "id_mesa": resultado.id_mesa
        }
        return result


    def update(self, id, data):
        resultado = Resultado2.query.get(id)
        resultado_votos = data['cantidad_votos']
        resultado_candidato = data['id_candidato']
        resultado_mesa = data['id_mesa']
        if resultado is None:
            respuesta = {
                "success": False,
                "response": "No se encontró el resultado"
            }
        else:
            resultado.cantidad_votos = resultado_votos
            resultado.id_candidato = resultado_candidato
            resultado.id_mesa = resultado_mesa
            db.session.merge(resultado)
            db.session.commit()
            respuesta = {
                "success": True,
                "response": "Resultado actualizado exitosamente"
            }
        return respuesta


    def delete(self, id):
        resultado = Resultado2.query.get(id)
        if resultado is None:
            respuesta = {
                "success": False,
                "response": "No se encontró el resultado"
            }
        else:
            db.session.delete(resultado)
            db.session.commit()
            respuesta = {
                "success": True,
                "response": "Resultado eliminado exitosamente"
            }
        return respuesta