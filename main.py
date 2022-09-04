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


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Dataconfig:", dataConfig)
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])