const express = require('express');
const app = express();
app.use(express.json());

const mensagens = {};

app.post('/enviar', (req, res) => {
    const { remetente, destinatario, conteudo } = req.body;
    if (!mensagens[destinatario]) mensagens[destinatario] = [];
    mensagens[destinatario].push({ remetente, conteudo, timestamp: Date.now() });
    res.json({ msg: 'Mensagem enviada' });
});

app.get('/mensagens/:usuario', (req, res) => {
    const usuario = req.params.usuario;
    res.json(mensagens[usuario] || []);
});

app.listen(3000, () => console.log('Servidor de mensagens rodando na porta 3000'));