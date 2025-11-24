# app.py
import streamlit as st
import requests

st.set_page_config(page_title="HealthTriage IA", page_icon="🏥")

st.title("🏥 HealthTriage: Classificação Inteligente")
st.write("Descreva o que o paciente está sentindo para obter uma classificação de triagem.")

symptom = st.text_area("Descrição do Sintoma", "Estou sentindo uma dor forte no peito e falta de ar.")

if st.button("Classificar Urgência"):
    if symptom:
        with st.spinner('Consultando a IA...'):
            try:
                # Conecta com nossa API (Backend)
                response = requests.post("http://127.0.0.1:8000/triagem", json={"description": symptom})
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"Categoria: **{data['categoria_sugerida']}**")
                    st.info(f"Confiança do Modelo: {data['confianca']}")
                else:
                    st.error("Erro na comunicação com a API.")
            except Exception as e:
                st.error(f"O backend parece estar desligado. Erro: {e}")
    else:
        st.warning("Por favor, digite um sintoma.")