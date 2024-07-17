from flask import Flask, request, jsonify, render_template
import os
from datetime import datetime
from werkzeug.utils import secure_filename
import uuid  # Importa o módulo uuid para gerar nomes de arquivo únicos

app = Flask(__name__)

# Diretório onde o aplicativo está localizado
app_root = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Verifica se a requisição contém um arquivo
        if 'file' not in request.files:
            return jsonify({'error': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['file']

        # Verifica se o nome do arquivo é válido
        if file.filename == '':
            return jsonify({'error': 'Nome do arquivo não especificado'}), 400

        # Diretório para salvar os uploads dentro da pasta 'app'
        upload_dir = os.path.join(app_root, 'uploads')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        # Gera um nome de arquivo único usando uuid
        filename = str(uuid.uuid4()) + '.jpg'  # Adiciona a extensão .jpg ao nome de arquivo UUID
        filename = secure_filename(filename)  # Garante que o nome de arquivo é seguro
        
        file.save(os.path.join(upload_dir, filename))

        return jsonify({'message': 'Foto recebida e salva com sucesso'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
