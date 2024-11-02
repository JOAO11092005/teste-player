from flask import Flask, render_template, Response
import requests

app = Flask(__name__)

VIDEO_URL = "http://cdn.teambr.live:80/movie/iptv0887/19971460887/49856.mp4"

def get_video_url():
    # Aqui você pode implementar a lógica para pegar e analisar a URL real
    # No exemplo, retornamos uma URL fixa, mas você pode implementar a lógica de extração
    return "http://66.90.84.42/vauth/AZB6XLAEwb9cVNs7R0Fq4bGidV5jiq7ymN47c_UJ1ILrvo6MJGJWS7suNjB03nhZmfttIXYdzOUW-29vvhV_km8XEK6MeLEcf1sUjnSZdg4h5T7EN0CXb3camVC4O_z6vh_3Rx3XT78OEx-jEfz95obHbKbEFrU-cYRFQadjzSQumOPB3crdNqk-m0aKPAmykLhZgXBEylPlRiQ9wfpJ33DcHexqcUIaJiLa5y98bxngLbzAIsKRt2o7dPtdCP9AY9PbpAJR13dbw_bw_2F_XOaXJy6O1w2DP3B-EQuzPqtl1bNL0hQLzkpGYb8dAdX-ee7OkMLSj5_oiMkS-RrnNsJUWjPgc-CJcOt4fW5apWbz3XXrnK8tUqOo7-1R5TgJm2kGG9tLOvpozMMKQp1GRa4KTMUlz1ER0zeZMuhB1iuXDJaRnkFRJM60UZuwqNCwv_MkZ4XRCkoP6ZH_oqiN8S_us2J_5lrflIwTckZrEgxqqnGipfDMrGkRz0vx5MYNdD8-8VyHYgG0p15JAzJsMp5xCWDBWL7WWT0b_8P_8sXC98ZDNSwAnVHm4sawqKcdiD7KjgpVdntvUWTI7LIe-FWi_IKetn9GbffuqD3uXYxh9o07eIutJEgWxK07gaQ1m722XoNzpg_Thv_UqWBLBLqqyIieV_HsWLZV513jjak"

@app.route('/')
def home():
    video_url = get_video_url()
    return render_template('index.html', video_url=video_url)

@app.route('/video')
def video():
    video_url = get_video_url()
    response = requests.get(video_url, stream=True)
    return Response(response.iter_content(chunk_size=4096),
                    content_type=response.headers['Content-Type'])

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use SSL para HTTPS
