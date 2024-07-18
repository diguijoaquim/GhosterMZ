# GhosterMZ created by Ghost04
#
# MIT License
#
# Copyright (c) 2024 Ghost04
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sqlalchemy
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,Integer,DateTime
import os
import subprocess
from db.model import *
# Obtém o caminho absoluto do diretório atual (onde o control.py está localizado)
current_dir = os.path.dirname(os.path.abspath(__file__))

        

# Constrói o caminho absoluto para o banco de dados
db_path = os.path.join(current_dir, 'db', 'dados.db')

# Cria a engine com o caminho absoluto do banco de dados
engine = sqlalchemy.create_engine(f"sqlite:///{db_path}", echo=False)


#Se o arquivo dados.db nao existir execute essa funcao
def criatar_tabela():
    Base.metadata.create_all(engine)

#Vamos criar a sessao db
Session=sessionmaker(bind=engine)
db=Session()

#Cadastra o Ataque no Banco De Dados

def AddAtack(dados):
    #tipo de dados a receber -->{"nome":"Ghosts04"}
    ataque=Ataque(type=dados['tipo'],ip=dados['ip'],latitude=dados['latitude'],longitude=dados['longitude'],username=dados['username'],password=dados['password'],datetime=dados['datetime'])
    db.add(ataque)
    db.commit()

#imprimir tudinho
def printAllAtack():
    atks=db.query(Ataque).all()
    # Definindo códigos de controle ANSI para cores
    GREEN = "\033[32m"
    WHITE = "\033[37m"
    RESET = "\033[0m"

    atks = db.query(Ataque).all()
    for i in atks:
        print(
            f"""
    {GREEN}Tipo:{RESET} {WHITE}{i.type}{RESET}
    {GREEN}IP:{RESET} {WHITE}{i.ip}{RESET}
    {GREEN}Latitude:{RESET} {WHITE}{i.latitude}{RESET}
    {GREEN}Longitude:{RESET} {WHITE}{i.longitude}{RESET}
    {GREEN}Usuario:{RESET} {WHITE}{i.username}{RESET}
    {GREEN}Senha:{RESET} {WHITE}{i.password}{RESET}
    {GREEN}Data:{RESET} {WHITE}{i.datetime}{RESET}
            """
        )




