from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = {}
postagens = []
seguidores = {}

@app.route('/criar_usuario', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    usuario = dados['usuario']
    if usuario in usuarios:
        return jsonify({'erro': 'Usuário já existe'}), 400
    usuarios[usuario] = {'nome': usuario}
    seguidores[usuario] = set()
    return jsonify({'msg': 'Usuário criado'}), 201

@app.route('/seguir', methods=['POST'])
def seguir():
    dados = request.get_json()
    seguidor = dados['seguidor']
    seguido = dados['seguido']
    if seguidor not in usuarios or seguido not in usuarios:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    seguidores[seguido].add(seguidor)
    return jsonify({'msg': f'{seguidor} está seguindo {seguido}'}), 200

@app.route('/postar', methods=['POST'])
def postar():
    dados = request.get_json()
    usuario = dados['usuario']
    conteudo = dados['conteudo']
    relogio_logico = dados.get('relogio_logico', 0)
    if usuario not in usuarios:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    postagens.append({
        'usuario': usuario,
        'conteudo': conteudo,
        'timestamp': relogio_logico
    })
    return jsonify({'msg': 'Postagem criada'}), 201

@app.route('/feed/<usuario>', methods=['GET'])
def feed(usuario):
    if usuario not in usuarios:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    seguidos = seguidores[usuario]
    feed_posts = [p for p in postagens if p['usuario'] == usuario or p['usuario'] in seguidos]
    feed_posts = sorted(feed_posts, key=lambda x: x['timestamp'], reverse=True)
    return jsonify(feed_posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)