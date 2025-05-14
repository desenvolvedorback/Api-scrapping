FROM python:3.12-slim

WORKDIR /app

COPY . .

# Corrige erro de "Pip: comando não encontrado" e instala dependências
RUN apt-get update && \
    apt-get install -y gcc && \
    pip install --upgrade pip setuptools build && \
    pip install .

# Define a porta do Flask
EXPOSE 5000

# Atalhos pro flask funcionar direto
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
