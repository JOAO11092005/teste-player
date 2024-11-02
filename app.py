from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/video')
def video():
    video_url = 'http://cdn.teambr.live:80/movie/iptv0887/19971460887/49856.mp4'
    response = requests.get(video_url, stream=True)

    return Response(response.iter_content(chunk_size=1024),
                    content_type='video/mp4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
