from flask import Flask
from flask import request
from pymongo import MongoClient
import random
import os 
from flask import jsonify

MONGO_SERVER = os.environ['MONGO_SERVER']

app = Flask(__name__)

def get_database():
    client = MongoClient(MONGO_SERVER)
    return client['acervo']

@app.route("/recomendar",methods=['GET'])
def gera_recomendacao():

    idUsuario = request.args.get("idUsuario")
    print(f"id usuario={idUsuario}")
    retorno = []
    
    db = get_database()
    colection = db['livros']

    for x in colection.find():
        retorno.append({'_id':str(x['_id']),'titulo':x['titulo'],'anoPublicacao':x['anoPublicacao'],'categoria':x['categoria']})

    random.shuffle(retorno)

    resposta = {'idUsuario':idUsuario,'recomendacoes':retorno[:3]}

    return jsonify(resposta)







