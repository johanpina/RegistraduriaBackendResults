from flask import jsonify, Blueprint, request
from Controladores.ControladorResultado import ControladorResultado

cont = ControladorResultado()

resultado = Blueprint('resultado',__name__)


@resultado.route("/resultados",methods=['GET'])
def getResultados():
    return jsonify(cont.index())


@resultado.route("/resultadoCreate",methods=['POST'])
def crearResultado():
    data = request.get_json()
    return jsonify(cont.create(data))


@resultado.route("/resultado/<string:id>",methods=['GET'])
def getResultado(id):
    return jsonify(cont.show(id))


@resultado.route("/resultadoUpdate/<string:id>",methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    return jsonify(cont.update(id,data))


@resultado.route("/resultadoDelete/<string:id>", methods = ['DELETE'])
def eliminarResultado(id):
    return jsonify(cont.delete(id))


@resultado.route("/votosPartido/<int:partidoId>",methods=['GET'])
def votosPartido(partidoId):
    return jsonify(cont.partido_votos(partidoId))


@resultado.route("/votosPartidos/",methods=['GET'] )
def listaVotosPartidos():
    return jsonify(cont.listaVotosPartidos())


@resultado.route("/votosMesa/<string:numeroMesa>",methods=['GET'])
def votosMesa(numeroMesa):
    return jsonify(cont.mesa_votos(numeroMesa))


@resultado.route("/votosMesas/",methods=['GET'] )
def listaVotosMesas():
    return jsonify(cont.listaVotosMesas())


@resultado.route("/votosCandidato/<string:cedula>",methods=['GET'])
def votosCandidato(cedula):
    return jsonify(cont.candidatosVotos(cedula))


@resultado.route("/votosCandidatos/",methods=['GET'] )
def listaVotosCandidatos():
    return jsonify(cont.listaVotosCandidatos())


@resultado.route("/totalVotos/",methods=['GET'] )
def getTotalVotos():
    return jsonify(cont.totalVotos())

