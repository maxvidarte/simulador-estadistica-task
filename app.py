import streamlit as st
import streamlit.components.v1 as components

# Configuración de pantalla completa en Streamlit
st.set_page_config(
    page_title="Simulador de Ejercicios de Estadística",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS para eliminar márgenes en el iframe de Streamlit
st.markdown("""
    <style>
        .block-container {
            padding: 0rem;
        }
        iframe {
            width: 100%;
            height: 100vh;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Leer y renderizar tu archivo HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=900, scrolling=True)