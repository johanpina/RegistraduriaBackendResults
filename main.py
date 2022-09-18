from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json
from waitress import serve
from flask_sqlalchemy import SQLAlchemy
from Routes.Mesa import mesa
from Routes.Partido import partido
from Routes.Candidato import candidato
from Routes.Resultado import resultado
from Routes.ResultadoBI import resultadoBi
from db import db

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

app.register_blueprint(mesa)
app.register_blueprint(partido)
app.register_blueprint(candidato)
app.register_blueprint(resultado)
app.register_blueprint(resultadoBi)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Dataconfig:", dataConfig)
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])