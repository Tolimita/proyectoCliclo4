from Modelos.Partido import Partido

class ControladorPartido():


    def __init__(self):
        print("Creando controlador   partido")

#Mostrar todos los partidos
    def index(self):
        print("Listar  todas los partidos")
        unPartido =[
            {
                 "Id": 1,
                 "Nombre": "Partido del cambio",
                 "Lema":"Somos mas"
            },
            {
                "Id": 2,
                "Nombre": "Partido solitario",
                "Lema":"Somos mejores"
            },
            {
                "Id": 3,
                "Nombre": "Parido del llano",
                "Lema":"El cambio es hoy."
            }
        ]
        return [unPartido]

#Crear un partido
    def create(self,infopartido):
        print("Crear un partido")
        elPartido = Partido(infopartido)
        return elPartido.__dict__

#Muestra un partido a traves del id
    def show(self, id):
        print("Mostrando un partido")
        elPartido = [
            {"Id": 2,
             "Nombre": "Partido solitario",
             "Lema": "Somos mejores"
             }
        ]

        return elPartido

#Actualiza el partido a traves del id
    def update(self, id, infoPartido):
        print("Actualizando partido con id ", id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def delete(self, id):
        print("Eliminando partido con numero ", id)
        return {"deleted_count":1}




