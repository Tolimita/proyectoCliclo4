from Modelos.Resultado import Resultado

class ControladorResultado():

    def __init__(self):
        print("Creando controlador resultado")

    def index(self):
        print("Listar  todas los resultados")
        unResultado = [
            {
                "Id": 1,
                "Numero Mesa": 10,
                "Id_Partido": 4
            }]
        return [unResultado]

    def create(self,infoResultado):
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def show(self, id):
        print("Mostrando un resultado")
        elResultado = {
            "Id": 1,
            "Numero Mesa": 4,
            "Id_partido": 4
        }
        return elResultado

    def update(self, id, infoDelaMesa):
        print("Actualizando resultado con id ", id)
        elResultado = Resultado(infoDelaMesa)
        return elResultado.__dict__

    def delete(self, id):
        print("Eliminando resultado con numero ", id)
        return {"deleted_count":1}
