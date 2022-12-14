from flask import jsonify, Blueprint, request
from Controladores.ControladorResultado import ControladorResultado

cont = ControladorResultado()

resultado = Blueprint('resultado',__name__)


@resultado.route("/resultados",methods=['GET'])
def getResultados():
    return jsonify(cont.index())


@resultado.route("/resultados",methods=['POST'])
def crearResultado():
    data = request.get_json()
    return jsonify(cont.create(data))


@resultado.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    return jsonify(cont.show(id))


@resultado.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    return jsonify(cont.update(id,data))


@resultado.route("/resultados/<string:id>", methods = ['DELETE'])
def eliminarResultado(id):
    return jsonify(cont.delete(id))
