
import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://UsuarioPruebas:123456abc@cluster0.cww4hty.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db = client.test
print(db)

baseDatos = client["BDVotacion"]
print(baseDatos.list_collection_names())

