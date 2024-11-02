from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

# Função para instalar os requisitos
def install_requirements():
    subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

@app.route('/')
def index():
    # Insira aqui a lógica para obter o link
    original_link = "http://38.99.239.203/deliver/20206.mp4?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEiLCJleHAiOjE3MzA2MDQ1ODJ9.eyJ1YyI6Ik9EYzJNRFUyIiwicGMiOiJVR0k1VTFsSyIsInN0IjoiMjAyMDYubXA0IiwiaXAiOiIxNDMuMjU1LjE0OC4xOTIifQ.cbFFzkYrR-aVQzUH-F0U8xricakSDgMVInQl3MwvH98&uc=ODc2MDU2&pc=UGI5U1lK"
    return render_template('index.html', video_link=original_link)

if __name__ == '__main__':
    install_requirements()  # Chama a função para instalar requisitos
    app.run(host='0.0.0.0', port=5000)
