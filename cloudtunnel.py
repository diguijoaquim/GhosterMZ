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




           






