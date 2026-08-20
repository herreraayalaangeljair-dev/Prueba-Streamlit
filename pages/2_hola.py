import streamlit as st

st.title("Esta es una pagina nueva")

nombre = st.text_input("Ingresa tu nombre")

if nombre:
    st.write(f"Mucho gusto {nombre}")

if st.button("Da un click"):
    st.success("Gracias por precionar mi boton :)")