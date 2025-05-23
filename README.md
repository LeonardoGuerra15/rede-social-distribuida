# Projeto de Sistema Distribuído - Rede Social
Este é um projeto acadêmico desenvolvido para a disciplina CC7261 - Sistemas Distribuídos, com o objetivo de aplicar conceitos de comunicação entre processos, consistência, sincronização de relógios e escalabilidade utilizando uma arquitetura de microserviços.
A aplicação simula uma rede social distribuída, onde é possível criar usuários, realizar postagens, seguir perfis, trocar mensagens privadas e sincronizar o tempo entre servidores.

## Visão Geral do Projeto
A rede social foi projetada para ser distribuída, escalável e resiliente, permitindo a adição e remoção dinâmica de servidores. Entre as principais funcionalidades, destacam-se:

- ✅ Publicação de textos com timestamp e associação ao usuário

- ✅ Sistema de seguidores, com notificações de novas postagens

- ✅ Mensagens privadas confiáveis e ordenadas

- ✅ Sincronização de relógios entre servidores usando algoritmos:

  -  Relógio lógico (Lamport) para ordenação de eventos

  - Berkeley com eleição de coordenador via algoritmo de bullying

- ✅ Replicação de dados entre múltiplos servidores backend

- ✅ Geração de logs por processo (postagens, mensagens, sincronização)


## Tecnologias utilizadas
| Serviço                           | Linguagem               | Framework/Biblioteca          |
| --------------------------------- | ----------------------- | ----------------------------- |
| Serviço de postagens e seguidores | Python                  | Flask                         |
| Serviço de mensagens privadas     | Node.js                 | Express.js                    |
| Sincronização de relógios         | Go                      | net/http + lógica customizada |
| Orquestração dos serviços         | Docker & Docker Compose |                               |

## 📁 Estrutura do Projeto

```plaintext
.
├── backend-python/
│   └── app.py
│
├── docker/
│   ├── backend-python.Dockerfile
│   ├── mensagens-node.Dockerfile
│   ├── replicacao.Dockerfile
│   └── sincronizacao-go.Dockerfile
│
├── mensagens-node/
│   └── index.js
│
├── replicacao/
│   └── replicador.py
│
├── sincronizacao-go/
│   └── main.go
│
├── docker-compose.yml
└── README.md
```

## Como Executar o Projeto

### Pré-requisitos:

- Docker

- Docker Compose


### Build e execução dos serviços:

```plaintext
docker-compose up --build
```

## Endpoints da API

### Backend Python (Postagens e Seguidores)

| Método | Endpoint          | Descrição                 |
| ------ | ----------------- | ------------------------- |
| POST   | `/criar_usuario`  | Cria um novo usuário      |
| POST   | `/seguir`         | Um usuário segue outro    |
| POST   | `/postar`         | Realiza uma postagem      |
| GET    | `/feed/<usuario>` | Retorna o feed do usuário |

### Backend Node.js (Mensagens Privadas)

| Método | Endpoint               | Descrição                    |
| ------ | ---------------------- | ---------------------------- |
| POST   | `/enviar`              | Envia uma mensagem privada   |
| GET    | `/mensagens/<usuario>` | Lista as mensagens recebidas |

### Serviço Go (Sincronização de Relógios)

| Método | Endpoint          | Descrição                                         |
| ------ | ----------------- | ------------------------------------------------- |
| POST   | `/registrar`      | Registra um servidor participante com sua hora    |
| GET    | `/berkeley`       | Executa o algoritmo de sincronização Berkeley     |
| GET    | `/horas`          | Mostra os horários dos servidores registrados     |
| POST   | `/relogio_logico` | Atualiza ou solicita incremento do relógio lógico |

## Especificação Técnica
- Cada usuário ou servidor mantém um relógio lógico (Lamport) para garantir ordenação causal das mensagens.

- O serviço de sincronização aplica o algoritmo Berkeley periodicamente, utilizando um coordenador eleito via bullying.

- Todos os processos geram logs em arquivos, contendo:

  - Publicações e autores

  - Relógio lógico associado

  - Mensagens enviadas e recebidas

  - Eventos de sincronização de tempo


## Diagrama de Arquitetura
### {INSERIR}

## Considerações Finais
Este projeto visa aplicar conceitos fundamentais de sistemas distribuídos na prática, abordando:

- Microserviços e isolamento de responsabilidades

- Comunicação entre processos (HTTP REST)

- Ordenação e consistência de eventos com relógios lógicos

- Sincronização realista com algoritmo de Berkeley

- Resiliência e escalabilidade com Docker

## Alunos:


| Nome | RA               |
| ------ | ---------------------- |
| Leonardo Guerra Modesto       | 22.222.068-4  |
| Felipe Del'Amore da Cunha     | 22.120.085-0  |

