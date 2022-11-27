import json

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

'''Inicio de rutas controladoras de modelo mesa'''
from Controladores.ControladorMesa import ControladorMesa
miControladorMesa = ControladorMesa()


@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def crearMesa():
    print("crear Mesa")
    date = request.get_json()
    json = miControladorMesa.create(date)
    return jsonify(json)


@app.route("/mesas/<string:numero>", methods=['GET'])
def getMesa(numero):
    json = miControladorMesa.show(numero)
    return jsonify(json)


@app.route("/mesas/<string:numero>", methods=['PUT'])
def modificarMesa(numero):
    data = request.get_json()
    json = miControladorMesa.update(numero, data)
    return jsonify(json)


@app.route("/mesas/<string:numero>", methods=['DELETE'])
def eliminarMesa(numero):
    json = miControladorMesa.delete(numero)
    return jsonify(json)
'''Aqui finaliza las rutas controladoras del modelo mesa'''




'''Inicio de rutas controladoras de partido'''
from Controladores.ControladorPartido import ControladorPartido
miControladorPartido = ControladorPartido()


@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=['POST'])
def crearPartido():
    print("crear Partido")
    dato = request.get_json()
    json = miControladorPartido.create(dato)
    return jsonify(json)



@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)
'''Aqui finaliza las rutas controladoras del modelo partido'''


'''Inicio controladores candidato'''
from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato = ControladorCandidato()

@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos", methods=['POST'])
def crearCandidatos():
    print("crear Candidato")
    date = request.get_json()
    json = miControladorCandidato.create(date)
    return jsonify(json)


@app.route("/candidatos/<string:cedula>", methods=['GET'])
def getCandidato(cedula):
    json = miControladorCandidato.show(cedula)
    return jsonify(json)



@app.route("/candidatos/<string:cedula>", methods=['PUT'])
def modificarCandidatos(cedula):
    data = request.get_json()
    json = miControladorCandidato.update(cedula, data)
    return jsonify(json)

@app.route("/candidatos/<string:cedula>", methods=['DELETE'])
def eliminarCandidatos(cedula):
    json = miControladorCandidato.delete(cedula)
    return jsonify(json)
'''Fin controladores candidato'''


'''Inicio controladores resultado'''

from Controladores.ControladorResultado import ControladorResultado
miControladorResultado = ControladorResultado()

@app.route("/resultados", methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados", methods=['POST'])
def crearResultados():
    print("crear Resultado")
    dato = request.get_json()
    json = miControladorResultado.create(dato)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['PUT'])
def modificarResultados(id):
    data = request.get_json()
    json = miControladorResultado.update(id, data)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultados(id):
    json = miControladorResultado.delete(id)
    return jsonify(json)

'''Fin controladores resultado'''









@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Corriendo servidor : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
