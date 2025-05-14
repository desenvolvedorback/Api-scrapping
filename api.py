from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/analisar', methods=['POST'])
def analisar():
    dados = request.get_json()
    url = dados.get('url')

    if not url:
        return jsonify({'erro': 'URL não fornecida'}), 400

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({'erro': f'Erro {response.status_code} ao acessar a página'}), 500

        soup = BeautifulSoup(response.text, 'html.parser')
        resultado = {
            'titulo': soup.title.string if soup.title else "Sem título",
            'meta_tags': [],
            'paragrafos': [],
            'links': [],
            'imagens': []
        }

        for meta in soup.find_all('meta'):
            if meta.get("name"):
                resultado['meta_tags'].append({meta.get("name"): meta.get("content")})
            elif meta.get("property"):
                resultado['meta_tags'].append({meta.get("property"): meta.get("content")})

        for p in soup.find_all('p'):
            resultado['paragrafos'].append(p.get_text()[:200])  # Até 200 caracteres

        for a in soup.find_all('a', href=True):
            resultado['links'].append(a.get('href'))

        for img in soup.find_all('img', src=True):
            resultado['imagens'].append(img.get('src'))

        return jsonify(resultado)

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': f'Erro na requisição: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)