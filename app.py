from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para servir o arquivo .jsdos (caso o navegador não pegue direto do static)
@app.route('/static/games/<path:filename>')
def serve_game(filename):
    return send_from_directory('static/games', filename)

if __name__ == '__main__':
    app.run(debug=True)