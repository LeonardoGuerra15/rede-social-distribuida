FROM node:20-alpine
WORKDIR /app
COPY ../mensagens-node /app
RUN npm install express
EXPOSE 3000
CMD ["node", "index.js"]