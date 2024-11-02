from flask import Flask, render_template, Response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# URL do site onde o vídeo está hospedado
SOURCE_URL = "https://teste-player.onrender.com/"  # Coloque aqui o URL da página que contém o vídeo

def get_video_url():
    # Faz uma requisição para o site e analisa o conteúdo
    response = requests.get(SOURCE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Tenta encontrar o link do vídeo
    video_tag = soup.find('video')
    if video_tag:
        source_tag = video_tag.find('source')
        if source_tag and 'src' in source_tag.attrs:
            return source_tag['src']
    
    return None  # Retorna None se não encontrar o link

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/video')
def video():
    video_url = get_video_url()
    if video_url:
        response = requests.get(video_url, stream=True)
        return Response(response.iter_content(chunk_size=4096), 
                        content_type=response.headers['Content-Type'])
    else:
        return "Video not found", 404

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use SSL para HTTPS
