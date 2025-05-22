import requests
import time

SERVIDORES = [
    'http://localhost:5000',
    'http://localhost:5001',
    'http://localhost:5002'
]

def obter_postagens(servidor):
    try:
        r = requests.get(f'{servidor}/feed/admin')
        if r.status_code == 200:
            return r.json()
    except:
        return []

def replicar():
    while True:
        print('Iniciando replicacao...')
        todas_postagens = []
        for srv in SERVIDORES:
            postagens = obter_postagens(srv)
            todas_postagens.extend(postagens)

        visto = set()
        unicas = []
        for p in todas_postagens:
            chave = (p['usuario'], p['conteudo'], p['timestamp'])
            if chave not in visto:
                visto.add(chave)
                unicas.append(p)

        for srv in SERVIDORES:
            for p in unicas:
                try:
                    requests.post(f'{srv}/postar', json={
                        'usuario': p['usuario'],
                        'conteudo': p['conteudo'],
                        'relogio_logico': p['timestamp']
                    })
                except:
                    pass

        print('Replicacao concluida.')
        time.sleep(10)

if __name__ == '__main__':
    replicar()