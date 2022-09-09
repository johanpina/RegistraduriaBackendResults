from flask import jsonify, Blueprint, request
from Controladores.controladorCandidato import ControladorCandidato

cont = ControladorCandidato()

candidato = Blueprint('candidato',__name__)

@candidato.route("/candidatos",methods=['GET'])
def getCandidatos():
    return jsonify(cont.index())


@candidato.route("/candidatoCreate",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    return jsonify(cont.create(data))


@candidato.route("/candidato/<string:cedula>",methods=['GET'])
def getCandidato(cedula):
    return jsonify(cont.show(cedula))


@candidato.route("/candidatoUpdate/<string:cedula>",methods=['PUT'])
def modificarCandidato(cedula):
    data = request.get_json()
    return jsonify(cont.update(cedula, data))


@candidato.route("/candidatoRemove/<string:cedula>",methods=['DELETE'])
def eliminarEstudiante(cedula):
    return jsonify(cont.delete(cedula))
