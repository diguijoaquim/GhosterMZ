# GhosterMZ
<img src='/demo/screenshot.png'>

## Version: 1.0.0

### Overview
GhosterMZ is a tool designed to demonstrate how website phishing works. My name is Dique Joaquim, a programmer in JavaScript and Python from Mozambique. I created this tool to challenge and showcase my knowledge. This project was inspired by htr-tech's zphisher (https://github.com/htr-tech/zphisher), which is written in Bash and PHP. GhosterMZ is built using Python with the Flask framework for backend and HTML, CSS, and JavaScript for frontend.

## Getting Started
To use GhosterMZ, you'll need a Linux terminal on either a computer or Android device, along with Python 3 installed. The tool uses Flask and cloudflared for tunneling. Installation is simplified with a Python script that detects your machine's architecture and downloads the appropriate files.

### Installation
<h4>Before cloning, please increase the buffer size:</h4>

```bash
git config --global http.postBuffer 524288000
```

Clone the repository:
```bash
git clone https://github.com/diguijoaquim/GhosterMZ.git
```
Open the Folder
```bash
cd GhosterMZ
```
Install required libs (Instalar as bibliotecas necessárias)
```bash
pip install -r requirements.txt
```
### Test Run (rodar a ferramenta)
First we need configure the tunnel(Configurar o túnel)
```bash
python cloudtunnel.py
```
and run the tool (e execute a ferramenta)
```bash
python ghostermz.py
```
<h1>Tested in google cloud shell<h1>
<p align="left">
  <a href="https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/diguijoaquim/GhosterMZ.git&cloudshell_open_in_editor=README.md" target="_blank">
    <img src="https://gstatic.com/cloudssh/images/open-btn.svg">
  </a>
</p>
<h3 style="color:orange">Aviso (Warning)</h3>
<p>Testei este projeto no Google Cloud Shell e um dos problemas encontrados foi com o SQLAlchemy. Por isso, precisei desinstalá-lo do Python 2.7 e instalá-lo no Python 3.10.</p>

<p>I tested this project on Google Cloud Shell and one of the issues was with SQLAlchemy. Therefore, I had to uninstall SQLAlchemy from Python 2.7 and install it for Python 3.10.</p>
<h2>Fixing (Resolvendo)</h2>

```bash
python2.7 -m pip uninstall sqlalchemy
python2.7 -m pip uninstall importlib-metadata
python3.10 -m pip install sqlalchemy
python3.10 -m pip install -r requirements.txt
```

<h2>Running the ghostermz.py and on google cloud shell</h2>
<img src="/demo/running1.png" alt="Imagem 1" width='500'>
    
<h2>Running the cloudtunel.py on google cloud shell</h2>
<img src="/demo/running.png" alt="Imagem 2" width='500'>


<h2>Me encontre no:</h2>
<a href='https://www.facebook.com/profile.php?id=100091313717660'>
facebook
  <img src='https://scontent-jnb2-1.xx.fbcdn.net/v/t39.30808-6/448274077_389307437456377_8308827626474677469_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeFdVMDKAaxZDX_-u-btuQWv1jS3z4zVTi_WNLfPjNVOL4xj8j6UJUxLiPM0SZdaLI6mMCIewY0LQVCaM-V0ziS1&_nc_ohc=8ZnOV7ubqo4Q7kNvgEBpovy&_nc_ht=scontent-jnb2-1.xx&oh=00_AYBN9aLEyUz9GByvuHhMkvo2J6-PMNYPkZLMBvt9wDc9AQ&oe=669F0988' width='80' height='80' label='facebook Dique Joaquim'>
</a>
<a href='https://www.youtube.com/@ghost404-'>
youtube
  <img src='https://yt3.googleusercontent.com/pGY-ybUOED5IcNrKBr0OG9K2CHzHBaA34Fzj8JmJZHJuRzEfkUfzokPQvLG-3CBRx4pBXtjfrQ=s160-c-k-c0x00ffffff-no-rj' width='80' height='80' label='facebook Dique Joaquim'>
</a>
