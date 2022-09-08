from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from Controladores.controladorCandidato import ControladorCandidato
miControladorCandidato = ControladorCandidato()
from Controladores.ControladorPartido import ControladorPartido
miControladorPartido = ControladorPartido()
from Controladores.ControladorMesa import ControladorMesa
miControladorMesa = ControladorMesa()


#db.create_all()
from Modelos import Candidato2
from Modelos import Mesa2

#Método para crear un registro
@app.route("/candidatoCreate",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    candidato_cedula  = data['cedula']
    candidato_nombre =  data['nombre']
    candidato_apellido = data['apellido']
    candidato_numero_res = data['numero_res']
    candidato_correo = data['correo']
    elcandidato = Candidato2.Candidato2(candidato_cedula, candidato_nombre, candidato_apellido, candidato_numero_res, candidato_correo)
    db.session.add(elcandidato)
    db.session.commit()
    return jsonify({"success": True,"response":"Candidato añadido"})

#Métido para obtener todos los registros
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    get_candidato = []
    candidatos = Candidato2.Candidato2.query.all()
    for candidato in candidatos:
        result = {
            "cedula": candidato.cedula,
            "nombre": candidato.nombre,
            "apellido": candidato.apellido,
            "numero_res": candidato.numero_res,
            "correo": candidato.correo
        }
        get_candidato.append(result)
    return jsonify(get_candidato)

#Método para obtener un solo registro
@app.route("/candidato/<string:cedula>",methods=['GET'])
def getCandidato(cedula):
    candidato = Candidato2.Candidato2.query.get(cedula)
    result = {
            "cedula": candidato.cedula,
            "nombre": candidato.nombre,
            "apellido": candidato.apellido,
            "numero_res": candidato.numero_res,
            "correo": candidato.correo
        }
    return jsonify(result)

@app.route("/candidatoUpdate/<string:cedula>",methods=['PUT'])
def modificarCandidato(cedula):
    candidato = Candidato2.Candidato2.query.get(cedula)
    data = request.get_json()
    candidato_nombre = data['nombre']
    candidato_apellido = data['apellido']
    candidato_numero_res = data['numero_res']
    candidato_correo = data['correo']
    if candidato is None:
        respuesta = {
            "success":False,
            "response": "No se encontró el candidato"
        }
    else:
        candidato.nombre = candidato_nombre
        candidato.apellido = candidato_apellido
        candidato.numero_res = candidato_numero_res
        candidato.correo = candidato_correo
        db.session.merge(candidato)
        db.session.commit()
        respuesta = {
            "success": True,
            "response": "Candidato actualizado"
        }
    return jsonify(respuesta)

@app.route("/candidatoRemove/<string:cedula>",methods=['DELETE'])
def eliminarEstudiante(cedula):
    candidato = Candidato2.Candidato2.query.get(cedula)
    print(candidato)
    if candidato is None:
        respuesta = {
            "success": False,
            "response": "No se encontró el candidato"
        }
    else:
        #db.session.delete(candidato)
        #db.session.commit()
        respuesta = {
            "success": True,
            "response": "Candidato eliminado"
        }
    return jsonify(respuesta)
#########################################################################################
#MESA!!!!
##Sección métodos Yuli ControladorMesa
@app.route("/mesaCreate",methods=['POST'])
def crearMesa():
    data = request.get_json()
    Mesa_Numero  = data['numero']
    Mesa_Ubicacion =  data['ubicacion']
    Mesa_Cantidad = data['cantidad']
    laMesa = Mesa2.Mesa2(Mesa_Numero, Mesa_Ubicacion, Mesa_Cantidad)
    db.session.add(laMesa)
    db.session.commit()
    return jsonify({"success": True,"response":"Mesa creada satisfactoriamente "})

@app.route("/Mesas",methods=['GET'])
def getMesas():
    get_mesa = []
    mesas = Mesa2.Mesa2.query.all()
    for mesa in mesas:
        result = {
            "numero": mesa.Numero,
            "ubicacion": mesa.Ubicacion,
            "cantidad": mesa.Cantidad,

        }
        get_mesa.append(result)
    return jsonify(get_mesa)

@app.route("/mesa/<string:numero>",methods=['GET'])
def getMesa(numero):
    mesa = Mesa2.Mesa2.query.get(numero)
    result = {
        "numero": mesa.Numero,
        "ubicacion": mesa.Ubicacion,
        "cantidad": mesa.Cantidad,
    }
    return jsonify(result)

@app.route("/mesaUpdate/<string:numero>",methods=['PUT'])
def modificarMesa(numero):
    mesa = Mesa2.Mesa2.query.get(numero)
    data = request.get_json()
    mesa_ubicacion = data['ubicacion']
    mesa_cantidad = data['cantidad']

    if mesa is None:
        respuesta = {
            "success": False,
            "response": "No se encontró la mesa"
        }
    else:
        mesa.Ubicacion = mesa_ubicacion
        mesa.Cantidad = mesa_cantidad
        db.session.merge(mesa)
        db.session.commit()
        respuesta = {
            "success": True,
            "response": "Mesa actualizada"
        }
    return jsonify(respuesta)



#########################################################################################

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

@app.route("/candidatoRemove2/<string:id>",methods=['DELETE'])
def eliminarEstudiante2(id):
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