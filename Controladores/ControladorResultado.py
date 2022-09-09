from Modelos.Resultado2 import Resultado2
from db import db
from Modelos.Partido2 import Partido2
from Modelos.Candidato2 import Candidato2
from Modelos.Mesa2 import Mesa2

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

    #Lógica para partidos

    def partido_votos(self, partidoId):
        resultados = Resultado2.query.all()
        votos = 0
        for resultado in resultados:
            candidato = Candidato2.query.get(resultado.id_candidato)
            if candidato.partido_id == partidoId:
                votos = votos + resultado.cantidad_votos
        respuesta = {
            "Partido": Partido2.query.get(partidoId).nombre,
            "Total de votos": votos
        }
        return respuesta

    def listaVotosPartidos(self):
        partidos = Partido2.query.all()
        lista_partidos = []
        for partido in partidos:
            lista_partidos.append(self.partido_votos(partido.id))
        return lista_partidos

    # Lógica para mesas
    def mesa_votos(self,mesa_numero):
        resultados = Resultado2.query.all()
        votos = 0
        for resultado in resultados:
            if resultado.id_mesa == mesa_numero:
                votos = votos + resultado.cantidad_votos
        respuesta = {
            "Mesa": mesa_numero,
            "Total de votos": votos
        }
        return respuesta

    def listaVotosMesas(self):
        mesas = Mesa2.query.all()
        lista_mesas = []
        for mesa in mesas:
            lista_mesas.append(self.mesa_votos(mesa.Numero))
        return lista_mesas

    #Lógica para candidatos
    def candidatosVotos(self,id_candidato):
        resultados = Resultado2.query.all()
        votos = 0
        candidato = Candidato2.query.get(id_candidato)
        for resultado in resultados:
            if resultado.id_candidato == id_candidato:
                votos = votos + resultado.cantidad_votos
        respuesta = {
            "Nombre candidato": candidato.nombre,
            "Apellido candidato": candidato.apellido,
            "Total de votos": votos
        }
        return respuesta

    def listaVotosCandidatos(self):
        candidatos = Candidato2.query.all()
        lista_candidatos = []
        for candidato in candidatos:
            lista_candidatos.append(self.candidatosVotos(candidato.cedula))
        return lista_candidatos

    #TOTAL DE VOTOS
    def totalVotos(self):
        resultados = Resultado2.query.all()
        votos = 0
        for resultado in resultados:
            votos = votos + resultado.cantidad_votos
        respuesta = {
            "Total de votos: ": votos
        }
        return respuesta