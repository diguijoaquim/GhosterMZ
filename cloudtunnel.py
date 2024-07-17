import platform
import subprocess
import os

filename="cloudflared"
def start():
    if os.path.exists(filename):
        try:
            p = str(input("\033[93mDigite a porta do host: \033[0m"))  # Amarelo para o texto do input
            subprocess.run([f'./cloudflared', 'tunnel', '-url', f'http://localhost:{p}'])
        except:
            print("\033[91mfechou o app\033[0m")  # Vermelho para o texto de fechamento
            
        
    else:
        download()

def download():
    if platform.system()=='Windows':
        print("Esta ferramenta so esta disponivel no linux e android")
    arch=platform.machine()
    print(arch)
    
    if os.path.exists(filename):
        start()
    else:
        if 'arm' in arch or 'Android' in arch:
            url='https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm'
            subprocess.run(['wget', '-O', filename, url])
        elif 'aarch64' in arch:
            url = 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64'
            subprocess.run(['wget', '-O', filename, url])
        elif 'x86_64' in arch:
            url='https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386'
            subprocess.run(['wget', '-O', filename, url])
            subprocess.run(["chmod", "+x", 'cloudflared'], check=True)
        elif 'AMD64'==arch:
            url="https://github.com/cloudflare/cloudflared/releases/download/2024.6.1/cloudflared-linux-amd64"
            subprocess.run(['wget', '-O', filename, url])
            subprocess.run(["chmod", "+x", 'cloudflared'], check=True)
        else:
            print("Maquina nao suportada -> fale com Ghost04 para adicionar essa arquiterura")
            
#o start ele verifica se o file existe ou nao ele chama a funacao download()
start()




           






