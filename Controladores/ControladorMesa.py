from Modelos.Mesa2 import Mesa2
from db import db
class ControladorMesa():

    def __init__(self):
        print("Creando una Mesa")

    def index(self):
        #Lista todas las mesas
        get_mesa = []
        mesas = Mesa2.query.all()
        for mesa in mesas:
            result = {
                "numero": mesa.Numero,
                "ubicacion": mesa.Ubicacion,
                "cantidad": mesa.Cantidad,

            }
            get_mesa.append(result)
        return get_mesa

    def create(self, data):
        #Creación de una mesa
        Mesa_Numero = data['numero']
        Mesa_Ubicacion = data['ubicacion']
        Mesa_Cantidad = data['cantidad']
        laMesa = Mesa2(Mesa_Numero, Mesa_Ubicacion, Mesa_Cantidad)
        db.session.add(laMesa)
        db.session.commit()
        respuesta = {
            "success": True,
            "response": "Mesa creada satisfactoriamente "
        }
        return respuesta

    def show(self, numero):
        #Muestra una mesa
        mesa = Mesa2.query.get(numero)
        result = {
            "numero": mesa.Numero,
            "ubicacion": mesa.Ubicacion,
            "cantidad": mesa.Cantidad,
        }
        return result

    def update(self,numero,data):
        mesa = Mesa2.query.get(numero)
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
        return respuesta

    def delete(self, numero):
        #Elimina una mesa
        mesa = Mesa2.query.get(numero)
        if mesa is None:
            respuesta = {
                "success": False,
                "response": "No se encontró la mesa"
            }
        else:
            db.session.delete(mesa)
            db.session.commit()
            respuesta = {
                "success": True,
                "response": "Mesa eliminada con éxito"
            }
        return respuesta