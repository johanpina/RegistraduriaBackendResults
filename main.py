from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve


app = Flask(__name__)
cors = CORS(app)


from Controladores.controladorCandidato import ControladorCandidato
miControladorCandidato = ControladorCandidato()
from Controladores.ControladorPartido import ControladorPartido
miControladorPartido = ControladorPartido()
from Controladores.ControladorMesa import ControladorMesa
miControladorMesa = ControladorMesa()



def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

## Sección Metodos Johan ControladorCandidatos

@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)


@app.route("/candidatoCreate",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatoUpdate/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id,data)
    return jsonify(json)


@app.route("/candidatoRemove/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)

##
##Sección métodos ruben ControladorPartidos

@app.route("/partidos",methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidoCreate",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partido/<string:id>",methods=['GET'])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidoUpdate/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/partidoRemove/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

##
##Sección métodos Yuli ControladorMesa

@app.route("/Mesas",methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesaCreate",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesa/<string:numero>",methods=['GET'])
def getMesa(numero):
    json = miControladorMesa.show(numero)
    return jsonify(json)

@app.route("/mesaUpdate/<string:numero>",methods=['PUT'])
def modificarMesa(numero):
    data = request.get_json()
    json = miControladorMesa.update(numero,data)
    return jsonify(json)

@app.route("/mesaRemove/<string:numero>",methods=['DELETE'])
def eliminarMesa(numero):
    json=miControladorMesa.delete(numero)
    return jsonify(json)

##

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Dataconfig:", dataConfig)
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])