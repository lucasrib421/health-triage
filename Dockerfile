# 1. Imagem Base: Começamos com um Python leve oficial
FROM python:3.10-slim

# 2. Pasta de Trabalho: Cria uma pasta dentro do container para colocar nosso app
WORKDIR /app

# 3. Otimização de Cache: Copiamos primeiro o requirements
# Isso faz com que o Docker não precise baixar tudo de novo se você só mexer no código
COPY requirements.txt .

# 4. Instalação: Instala as dependências dentro do container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Cópia do Código: Pega tudo da sua pasta atual e joga para dentro da pasta /app do container
COPY . .

# 6. Porta: Avisa ao Docker que esse container vai usar a porta 8000
EXPOSE 8000

# 7. Comando Inicial: O que roda quando o container liga?
# Aqui vamos subir a API (FastAPI)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]