from flask import jsonify, Blueprint, request
from Controladores.ControladorMesa import ControladorMesa

cont = ControladorMesa()

mesa = Blueprint('estudiante',__name__)

@mesa.route("/mesas",methods=['GET'])
def getMesas():
    return jsonify(cont.index())

@mesa.route("/mesaCreate",methods=['POST'])
def crearMesa():
    data = request.get_json()
    return jsonify(cont.create(data))

@mesa.route("/mesa/<string:numero>",methods=['GET'])
def getMesa(numero):
    return jsonify(cont.show(numero))

@mesa.route("/mesaUpdate/<string:numero>",methods=['PUT'])
def modificarMesa(numero):
    data = request.get_json()
    return jsonify(cont.update(numero, data))

@mesa.route("/mesaRemove/<string:numero>",methods=['DELETE'])
def eliminarMesa(numero):
    return jsonify(cont.delete(numero))