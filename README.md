# 🏥 HealthTriage - AI Powered Triage System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED)
![Tests](https://img.shields.io/badge/Pytest-Passing-brightgreen)
![HuggingFace](https://img.shields.io/badge/AI-mDeBERTa-yellow)

## 📋 Sobre o Projeto

O **HealthTriage** é uma prova de conceito (PoC) de um sistema de triagem inteligente. O objetivo é utilizar Processamento de Linguagem Natural (NLP) para classificar automaticamente a urgência e a categoria de sintomas descritos por pacientes em linguagem natural.

### 💡 Diferenciais de Engenharia
1.  **Zero-Shot Learning:** Resolve o problema do "Cold Start" (falta de dados históricos) utilizando inferência sem treinamento prévio.
2.  **Multilíngue:** Utiliza o modelo `mDeBERTa-v3` otimizado para compreender nuances do português brasileiro (gírias, erros gramaticais).
3.  **Arquitetura de Microsserviços:** Backend e Frontend desacoplados.

### 🎯 Contexto de Negócio
Embora aplicado à saúde, esta arquitetura é replicável para **classificação de tickets de suporte (Customer Service)**, triagem de reviews ou moderação de conteúdo — cenários comuns em plataformas de delivery e e-commerce.

---

## 🏗️ Arquitetura

O projeto utiliza uma arquitetura containerizada para garantir reprodutibilidade.

```mermaid
graph LR
    A[Usuário] -->|Interage| B(Frontend - Streamlit)
    B -->|Envia Sintoma (JSON)| C{API - FastAPI}
    subgraph Docker Container
        C
        D[Modelo Hugging Face<br/>mDeBERTa-v3]
    end
    C <-->|Inferência| D
    C -->|Retorna Classificação| B
```

## 🚀 Tecnologias
IA/NLP: MoritzLaurer/mDeBERTa-v3-base-mnli-xnli (Hugging Face).

Backend: FastAPI (Alta performance, validação Pydantic).

Frontend: Streamlit (Prototipagem rápida).

Infraestrutura: Docker.

Qualidade: Pytest (Testes de Integração).

## 📦 Como Rodar o Projeto

Você pode rodar o projeto de duas formas: Docker (Recomendado) ou Manualmente.

1. Via Docker 🐳 (Recomendado)

Garanta que o ambiente seja idêntico ao de produção.

Clone o repositório:

```bash
git clone [https://github.com/lucasrib421/health-triage.git](https://github.com/lucasrib421/health-triage.git)
cd health-triage
```

2. Construa a Imagem:

```bash
docker build -t health-triage-api .
```

3. Rode o Container (Backend):

```bash
docker run -d -p 8000:8000 health-triage-api
```
4. Inicie o Frontend: Em um terminal local (fora do Docker):

```bash
pip install streamlit requests
streamlit run app.py
```
### Opção 2: Instalação Manual 🛠️

1. Crie o ambiente virtual:

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Rode a API:

```bash
uvicorn main:app --reload
```
4. Rode o Frontend (em outro terminal):

```bash
streamlit run app.py
```
## ✅ Testes Automatizados
Para garantir a integridade da API e o contrato de dados, execute os testes de integração:
```bash
pytest
```
O teste verifica endpoints, validação de tipos e códigos de status HTTP.

## 📂 Estrutura de Arquivos

health-triage/
├── Dockerfile           # Receita para criar o container da API
├── app.py               # Interface do Usuário (Streamlit)
├── main.py              # Rotas da API (FastAPI)
├── service.py           # Lógica de IA e download do Modelo
├── requirements.txt     # Dependências do projeto
├── test_core.py         # Testes automatizados
└── README.md            # Documentação