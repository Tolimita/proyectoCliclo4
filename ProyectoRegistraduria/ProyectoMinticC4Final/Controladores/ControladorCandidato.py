from Modelos.Candidato import Candidato

class ControladorCandidato():
    def __init_(self):
        print("Creando controlador candidato")

    def index(self):
        print("Listar  todos los candidatos")
        unCandidato = [
            {
                "Cedula": 101010,
                "Numero Resolucion": 2,
                "Nombre": "Mariano",
                "Apellido": "Guzman"
            },
            {
                "Cedula": 22222,
                "Numero Resolucion": 3,
                "Nombre": "Josue",
                "Apellido" : "Beltran"
            }
        ]
        return [unCandidato]

    def create(self, infoCandidato):
        print("Crear un canditato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

        # Muestra un CANDIDATO a traves de LA CEDULA

    def show(self, cedula):
        print("Mostrando un candidato")
        elCandidato = {

                "Cedula": 22222,
                "Numero Resolucion": 3,
                "Nombre": "Josue",
                "Apellido": "Beltran"

        }
        return elCandidato

    def update(self, cedula, infoCandidato):
        print("Actualizando candidato con cedula ", cedula)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, cedula):
        print("Eliminando candidato con cedula ", cedula)
        return {"deleted_count":1}