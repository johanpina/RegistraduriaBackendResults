from Modelos.Partido2 import Partido2
from Modelos.Candidato2 import Candidato2
from Modelos.Mesa2 import Mesa2
from Modelos.Resultado2 import Resultado2

class ControladorResultadoBi():

    def __init__(self):
        "Creando el controlador de resultados"

        # Lógica para partidos

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
    def mesa_votos(self, mesa_numero):
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

    # Lógica para candidatos
    def candidatosVotos(self, id_candidato):
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

    # TOTAL DE VOTOS
    def totalVotos(self):
        resultados = Resultado2.query.all()
        votos = 0
        for resultado in resultados:
            votos = votos + resultado.cantidad_votos
        respuesta = {
            "Total de votos: ": votos
        }
        return respuesta