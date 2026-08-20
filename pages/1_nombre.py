import streamlit as st

st.set_page_config(page_title="Analizador sencillo de texto", page_icon="🥵",layout="centered")

st.title("Aquí vas a ingresar un string y recibir un análisis sencillo.")

texto_de_analisis = st.text_area("Ingresa un texrto cualquiera", placeholder="Ej. Mucho gusto, mi nombre es...")

if texto_de_analisis:
    palabras = texto_de_analisis.split()
    numero_palabras = len(palabras)
    numero_caracteres = len(texto_de_analisis)

    st.markdown("----------------------------------------------")
    st.subheader("Resultados :)")

    columna1, columna2 = st.columns(2)

    columna1.metric("Palabras", numero_palabras)
    columna2.metric("Caracteres",numero_caracteres)