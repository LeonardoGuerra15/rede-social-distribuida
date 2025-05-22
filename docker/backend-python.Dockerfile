FROM python:3.11-slim
WORKDIR /app
COPY ../backend-python /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]