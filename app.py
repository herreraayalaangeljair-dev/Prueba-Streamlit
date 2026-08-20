import streamlit as st
import pandas as pd

st.title("Primera prueba de streamlit con datos en archivo csv")

lectura = pd.read_csv("datos.csv")

st.dataframe(lectura)