from flask import jsonify, Blueprint, request
from Controladores.ControladorPartido import ControladorPartido

cont = ControladorPartido()

partido = Blueprint('partido',__name__)

@partido.route("/partidos",methods=['GET'])
def getPartidos():
    return jsonify(cont.index())


@partido.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    return jsonify(cont.create(data))


@partido.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    return jsonify(cont.show(id))


@partido.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    return jsonify(cont.update(id,data))


@partido.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    return jsonify(cont.delete(id))

