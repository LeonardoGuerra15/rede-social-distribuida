# Projeto de Sistema Distribuído - Rede Social

## Descrição
Rede social distribuída desenvolvida para a disciplina CC7261. O sistema permite:
- Criar usuários e realizar postagens
- Seguir outros usuários
- Trocar mensagens privadas
- Replicação de dados entre servidores
- Sincronização de relógios (Berkeley e Lamport)

## Tecnologias utilizadas
- **Python + Flask**: Serviço de postagens e seguir usuários
- **Node.js + Express**: Serviço de troca de mensagens
- **Go**: Serviço de sincronização de relógios
- **Docker + Docker Compose**: Orquestração dos serviços

## Como executar com Docker
```bash
docker-compose up --build
```

## Endpoints
### Backend Python (Postagens e Seguidores)
- `POST /criar_usuario` { "usuario": "nome" }
- `POST /seguir` { "seguidor": "user1", "seguido": "user2" }
- `POST /postar` { "usuario": "user", "conteudo": "texto", "relogio_logico": int }
- `GET /feed/<usuario>`

### Mensagens (Node.js)
- `POST /enviar` { "remetente": "user", "destinatario": "user", "conteudo": "texto" }
- `GET /mensagens/<usuario>`

### Sincronização (Go)
- `POST /registrar` { "nome": "srv", "hora": float }
- `GET /berkeley`
- `GET /horas`
- `POST /relogio_logico` { "relogio": int }

## Teste mínimo
- 3 servidores backend
- 1 serviço de mensagens
- 1 sincronizador de relógios
- 1 serviço de replicação
- Testes com no mínimo 5 usuários

## Extra
- Orquestração com Docker Compose
