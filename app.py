from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Removido o ssl_context para rodar sem HTTPS
    app.run(host='0.0.0.0', port=5000)
