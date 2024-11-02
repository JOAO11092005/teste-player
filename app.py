from flask import Flask, Response, request
import requests

app = Flask(__name__)

VIDEO_URL = "http://cdn.teambr.live:80/movie/iptv0887/19971460887/49856.mp4"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/video')
def video():
    response = requests.get(VIDEO_URL, stream=True)
    return Response(response.iter_content(chunk_size=4096), 
                    content_type=response.headers['Content-Type'])

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use SSL para HTTPS
