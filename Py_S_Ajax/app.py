from flask import Flask, render_template, request

app = Flask(__name__)

# Conjunto de dados de filmes
filmes = [
    {"nome": "O Homem de Ferro", "genero": "Ficção Científica"},
    {"nome": "Vovozona", "genero": "Comédia"},
    {"nome": "IT a coisa", "genero": "Terror"},
    {"nome": "Como treinar seu Dragão", "genero": "Animação"},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    sugestoes = []
    if request.method == 'POST':
        genero_preferido = request.form['genero'].capitalize()
        # Filtra os filmes com o gênero escolhido
        sugestoes = [f['nome'] for f in filmes if f['genero'] == genero_preferido]
    return render_template('index.html', sugestoes=sugestoes)

if __name__ == '__main__':
    app.run(debug=True)
