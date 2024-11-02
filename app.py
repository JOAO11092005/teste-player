from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-video', methods=['POST'])
def check_video():
    video_url = request.json['url']
    try:
        response = requests.head(video_url)
        if response.status_code == 200:
            return jsonify({'valid': True, 'url': video_url})
        else:
            return jsonify({'valid': False})
    except Exception as e:
        return jsonify({'valid': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
