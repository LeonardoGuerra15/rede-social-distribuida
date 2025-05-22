FROM python:3.11-slim
WORKDIR /app
COPY ../replicacao /app
RUN pip install requests
CMD ["python", "replicador.py"]