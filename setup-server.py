import platform
import subprocess
import os

# Verificar a arquitetura do sistema
arch = platform.machine()

if arch == "x86_64" or arch == "AMD64":
    # Nome do arquivo a ser baixado
    arquivo = "cloudflared--"
    
    # Caminho completo para o arquivo cloudflared
    cloudflared_path = os.path.abspath(arquivo)
    
    # Verificar se o arquivo já existe na pasta
    if os.path.exists(cloudflared_path):
        print(f"O arquivo '{cloudflared_path}' já existe.")
    else:
        # URL do arquivo a ser baixado
        url = "https://github.com/cloudflare/cloudflared/releases/download/2024.6.1/cloudflared-linux-amd64"
        
        # Comando wget com opção -O para especificar o nome do arquivo
        command = ["wget", "-O", arquivo, url]
        
        try:
            # Executar o comando wget
            subprocess.run(command, check=True)
            print(f"Arquivo baixado com sucesso de {url} e salvo como '{arquivo}'")
            
            # Definir permissões para o arquivo
            subprocess.run(["chmod", "+x", cloudflared_path], check=True)
            print(f"Permissões definidas para o arquivo '{cloudflared_path}'")
            
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o wget: {e}")
            exit(1)
    
    # Executar o comando cloudflared tunnel
    try:
        subprocess.run(["./" + arquivo, "tunnel", "-url", "http://localhost:5000"], check=True)
        print(f"Comando 'cloudflared tunnel' executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar 'cloudflared tunnel': {e}")
        exit(1)
        
else:
    print(f"A arquitetura do sistema não é compatível: {arch}")
    exit(1)
