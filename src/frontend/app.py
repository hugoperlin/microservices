
from flask import Flask
from flask import render_template
from flask import request   
import xmlrpc.client
import os
import sys
import requests as http_requests
import json

ACERVO_URL=os.environ['ACERVO_URL']
USUARIOS_URL=os.environ['USUARIOS_URL']
RECOMENDACOES_URL=os.environ['RECOMENDACOES_URL']

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/acervo",methods=['GET', 'POST'])
def acervo():
    
    print(f"ACERVO=>{ACERVO_URL}", file=sys.stderr)
    client = xmlrpc.client.ServerProxy(ACERVO_URL)
    
    if request.method == 'POST':
        dados = request.form.to_dict()
        client.adicionar_livro(dados)
    try:
        ret = client.listar_livros()
    except:
        return render_template('error.html')
    return render_template('acervo.html',livros=ret)

@app.route("/usuarios",methods=['GET', 'POST'])
def usuarios():
    print(f"USUARIOS=>{USUARIOS_URL}", file=sys.stderr)
    client = xmlrpc.client.ServerProxy(USUARIOS_URL)
    
    if request.method == 'POST':
        dados = request.form.to_dict()
        client.adicionar_usuario(dados)
    
    ret = client.listar_usuarios()
    return render_template('usuarios.html',usuarios=ret)

@app.route("/recomenda",methods=['GET'])
def recomenda():

    idUsuario = request.args.get('idUsuario')
    
    url = f"{RECOMENDACOES_URL}/recomendar?idUsuario={idUsuario}"
    print(url)
    response = http_requests.get(url)

    return render_template('recomendacoes.html',dados=json.loads(response.text))
