from flask import Flask, render_template, request, redirect, send_from_directory
from pytube import YouTube
import os
import random

app = Flask(__name__)

# Define um nome aleatório para os arquivos baixados
file_name = f"video_{random.randint(1, 1000000)}.mp4"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    global file_name
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        # Faz o download do vídeo com o nome definido no começo do código
        video.download(output_path='videos', filename=file_name)
        return redirect('/completed')
    else:
        return redirect('/')

@app.route('/completed')
def completed():
    # Retorna o arquivo com o nome definido no começo do código
    return send_from_directory("videos", file_name)

@app.route('/favicon')
def favicon():
    return send_from_directory('static', 'favicon.png', mimetype='image/png')

@app.route('/style.css')
def style():
    return send_from_directory('static', 'style.css', mimetype='text/css')

@app.route('/script.js')
def script():
    return send_from_directory('static', 'script.js', mimetype='application/javascript')


app.run(host='0.0.0.0', port=443, debug=True)

