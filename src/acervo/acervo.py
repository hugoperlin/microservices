from pymongo import MongoClient
import pymongo
from livro import Livro

import os

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_path=('/rpc')

MONGO_SERVER = os.environ['MONGO_SERVER']
print(MONGO_SERVER)
def get_database():
    client = MongoClient(MONGO_SERVER)
    return client['acervo']

def adicionar_livro(data):
    print("Adicionando livro")
    db = get_database()
    livro = Livro(**data)
    db.livros.insert_one(livro.toJson())

if __name__ == '__main__':
    server = SimpleXMLRPCServer(('0.0.0.0',8000),
                                requestHandler=RequestHandler)
    
    adicionar_livro({"titulo":"abc 123","anoPublicacao":2022,"categoria":1})

    print("Listening...")
    server.serve_forever()
