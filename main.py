from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from flask_sqlalchemy import SQLAlchemy
from Routes.Mesa import mesa
from Routes.Partido import partido
from Routes.Candidato import candidato
from db import db

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

app.register_blueprint(mesa)
app.register_blueprint(partido)
app.register_blueprint(candidato)

with app.app_context():
    db.create_all()

#Método para obtener un solo registro

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

#Sección de resultados
from Modelos import Resultado2

#Para crear un resultado
@app.route("/resultadoCreate",methods=['POST'])
def crearResultado():
    data = request.get_json()
    resultado_id = data['id']
    resultado_votos = data['cantidad_votos']
    resultado_candidato = data['id_candidato']
    resultado_mesa = data['id_mesa']
    elresultado = Resultado2.Resultado2(resultado_id, resultado_votos, resultado_candidato, resultado_mesa)
    db.session.add(elresultado)
    db.session.commit()
    return jsonify({"success": True, "response": "Resultado creado satisfactoriamente "})

@app.route("/resultados",methods=['GET'])
def getResultados():
    get_resultado = []
    resultados = Resultado2.Resultado2.query.all()
    for resultado in resultados:
        result = {
            "id": resultado.id,
            "cantidad_votos": resultado.cantidad_votos,
            "id_candidato": resultado.id_candidato,
            "id_mesa": resultado.id_mesa
        }
        get_resultado.append(result)
    return jsonify(get_resultado)

@app.route("/resultado/<string:id>",methods=['GET'])
def getResultado(id):
    resultado = Resultado2.Resultado2.query.get(id)
    result = {
        "id": resultado.id,
        "cantidad_votos": resultado.cantidad_votos,
        "id_candidato": resultado.id_candidato,
        "id_mesa": resultado.id_mesa
    }
    return jsonify(result)

@app.route("/resultadoUpdate/<string:id>",methods=['PUT'])
def modificarResultado(id):
    resultado = Resultado2.Resultado2.query.get(id)
    data = request.get_json()
    resultado_votos = data['cantidad_votos']
    resultado_candidato = data['id_candidato']
    resultado_mesa = data['id_mesa']

    if resultado is None:
        respuesta = {
            "success": False,
            "response": "No se encontró el resultado"
        }
    else:
        resultado.cantidad_votos = resultado_votos
        resultado.id_candidato = resultado_candidato
        resultado.id_mesa = resultado_mesa
        db.session.merge(resultado)
        db.session.commit()
        respuesta = {
            "success": True,
            "response": "Resultado actualizado exitosamente"
        }
    return jsonify(respuesta)


#Logica para partidos
def partido_votos(partidoId):
    resultados = Resultado2.Resultado2.query.all()
    votos = 0
    for resultado in resultados:
        candidato = Candidato2.Candidato2.query.get(resultado.id_candidato)
        if candidato.partido_id == partidoId:
            votos = votos + resultado.cantidad_votos
    respuesta = {
        "Partido": Partido2.Partido2.query.get(partidoId).nombre,
        "Total de votos": votos
    }
    return respuesta

#Número de votos para un partido x
@app.route("/votosPartido/<int:partidoId>",methods=['GET'])
def votosPartido(partidoId):
    return jsonify(partido_votos(partidoId))

#Votos de todos los partidos
@app.route("/votosPartidos/",methods=['GET'] )
def listaVotosPartidos():
    partidos = Partido2.Partido2.query.all()
    lista_partidos = []
    for partido in partidos:
        lista_partidos.append(partido_votos(partido.id))
    return jsonify(lista_partidos)


#Logica para mesas
def mesa_votos(mesa_numero):
    resultados = Resultado2.Resultado2.query.all()
    votos = 0
    for resultado in resultados:
        if resultado.id_mesa == mesa_numero:
            votos = votos + resultado.cantidad_votos
    respuesta = {
        "Mesa": mesa_numero,
        "Total de votos": votos
    }
    return respuesta

#Número de votos por mesa x
@app.route("/votosMesa/<string:numeroMesa>",methods=['GET'])
def votosMesa(numeroMesa):
    return jsonify(mesa_votos(numeroMesa))

@app.route("/votosMesas/",methods=['GET'] )
def listaVotosMesas():
    mesas = Mesa2.Mesa2.query.all()
    lista_mesas = []
    for mesa in mesas:
        lista_mesas.append(mesa_votos(mesa.Numero))
    return jsonify(lista_mesas)


#Logica candidatos

def candidatosVotos(id_candidato):
    resultados = Resultado2.Resultado2.query.all()
    votos = 0
    candidato = Candidato2.Candidato2.query.get(id_candidato)
    for resultado in resultados:
        if resultado.id_candidato == id_candidato:
            votos = votos + resultado.cantidad_votos
    respuesta = {
        "Nombre candidato": candidato.nombre,
        "Apellido candidato": candidato.apellido,
        "Total de votos": votos
    }
    return respuesta

@app.route("/votosCandidato/<string:cedula>",methods=['GET'])
def votosCandidato(cedula):
    return jsonify(candidatosVotos(cedula))


@app.route("/votosCandidatos/",methods=['GET'] )
def listaVotosCandidatos():
    candidatos = Candidato2.Candidato2.query.all()
    lista_candidatos = []
    for candidato in candidatos:
        lista_candidatos.append(candidatosVotos(candidato.cedula))
    return jsonify(lista_candidatos)


#CALCULAR EL TOTAL DE VOTOS

@app.route("/totalVotos/",methods=['GET'] )
def getTotalVotos():
    resultados = Resultado2.Resultado2.query.all()
    votos = 0
    for resultado in resultados:
        votos = votos + resultado.cantidad_votos
    respuesta = {
        "Total de votos: ": votos
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


##Sección métodos ruben ControladorPartidos

@app.route("/partidoRemove/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Dataconfig:", dataConfig)
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])