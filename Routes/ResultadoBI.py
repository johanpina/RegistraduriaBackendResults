from flask import jsonify, Blueprint, request
from Controladores.ControladorResultadoBI import ControladorResultadoBi

cont = ControladorResultadoBi()

resultadoBi = Blueprint('resultadoBI',__name__)

@resultadoBi.route("/votosPartido/<int:partidoId>",methods=['GET'])
def votosPartido(partidoId):
    return jsonify(cont.partido_votos(partidoId))


@resultadoBi.route("/votosPartidos/",methods=['GET'] )
def listaVotosPartidos():
    return jsonify(cont.listaVotosPartidos())


@resultadoBi.route("/votosMesa/<string:numeroMesa>",methods=['GET'])
def votosMesa(numeroMesa):
    return jsonify(cont.mesa_votos(numeroMesa))


@resultadoBi.route("/votosMesas/",methods=['GET'] )
def listaVotosMesas():
    return jsonify(cont.listaVotosMesas())


@resultadoBi.route("/votosCandidato/<string:cedula>",methods=['GET'])
def votosCandidato(cedula):
    return jsonify(cont.candidatosVotos(cedula))


@resultadoBi.route("/votosCandidatos/",methods=['GET'] )
def listaVotosCandidatos():
    return jsonify(cont.listaVotosCandidatos())


@resultadoBi.route("/totalVotos/",methods=['GET'] )
def getTotalVotos():
    return jsonify(cont.totalVotos())