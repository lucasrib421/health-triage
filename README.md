# 🏥 HealthTriage - AI Powered Triage System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![HuggingFace](https://img.shields.io/badge/AI-Hugging%20Face-yellow)

## 📋 Sobre o Projeto

O **HealthTriage** é uma prova de conceito (PoC) de um sistema de triagem inteligente para a área da saúde. O objetivo é utilizar Processamento de Linguagem Natural (NLP) para classificar automaticamente a urgência e a categoria de sintomas descritos por pacientes.

O sistema resolve o problema do "Cold Start" (falta de dados históricos para treinamento) utilizando modelos de **Zero-Shot Classification** do Hugging Face.

### 🎯 Contexto de Negócio e Engenharia
Embora aplicado à saúde, este projeto demonstra uma arquitetura escalável para **classificação de tickets e suporte ao cliente**.

## 🚀 Tecnologias Utilizadas

* **Modelo de IA:** `facebook/bart-large-mnli` (via Hugging Face Transformers) para classificação Zero-Shot.
* **Backend:** FastAPI (alta performance e validação de dados automática).
* **Frontend:** Streamlit (interface amigável para validação do usuário).
* **Linguagem:** Python.

## 🏗️ Arquitetura

O projeto segue uma arquitetura desacoplada:

1.  **API de Inferência:** Um serviço REST que recebe texto e retorna probabilidades.
2.  **Interface de Usuário:** Uma aplicação web que consome a API.

## 📦 Como Rodar o Projeto

### Pré-requisitos
* Python 3.9 ou superior.
* Git.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/lucasrib421/health-triage.git]
   cd health-triage

2. **Crie um ambiente virtual e instale as dependências:**
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

3. **Inicie a API (Backend): Abra um terminal e rode:**

uvicorn main:app --reload

A API estará rodando em: http://127.0.0.1:8000

4. **Inicie o Frontend: Abra outro terminal (com o venv ativado) e rode:**

streamlit run app.py