from Modelos.Candidato import Candidato


class ControladorCandidato():

    def __init__(self):
        print("Creando ControladorCandidato")
        
    def index(self):
        print("Listar todos los candidatos")
        unCandidato = {
            "cedula": "100156893",
            "Numero_res": "C11",
            "Nombre":"Pepito",
            "Apellido": "Perez",
            "Correo": "correo@gmail.com"
        }
        otroCandidato = {
            "cedula": "1234567894",
            "Numero_res": "C11",
            "Nombre": "Pepito",
            "Apellido": "Perez",
            "Correo": "correo@gmail.com"
        }
        return [unCandidato, otroCandidato]

        
    def create(self,infocandidato):
        print("Crear un candidato")
        elcandidato = Candidato(infocandidato)
        return {"mensaje": "Candidato creado Satisfactoriamente", "candidato":elcandidato.__dict__}
        
    def show(self,id):
        print("Mostrando un candidato con id ", id)
        unCandidato = {
            "id_": 1,
            "cedula": "100156893",
            "Numero_res": "C11",
            "Nombre": "Pepito",
            "Apellido": "Perez",
            "Correo": "correo@gmail.com"
        }
        return unCandidato

    def update(self, id, infoCandidato):
        print("Actualizando candidato con id ", id)
        elCandidato = Candidato(infoCandidato)
        return {"mensaje": "Candidato actualizado Satisfactoriamente", "candidato":elCandidato.__dict__}

    def delete(self, id):
        print("Elimiando candidato con id ", id)
        return {"mensaje": "Candidato eliminado Correctamente"}