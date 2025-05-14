# Etapa 1: base com Python
FROM python:3.12-slim AS base

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Cria ambiente virtual e instala ferramentas de build
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip setuptools build && \
    pip install .

# Usa o ambiente virtual como padrão
ENV PATH="/opt/venv/bin:$PATH"

# Porta usada pela aplicação Flask
EXPOSE 5000

# Comando padrão para rodar o app (ajuste conforme seu arquivo principal)
CMD ["flask", "run", "--host=0.0.0.0"]
