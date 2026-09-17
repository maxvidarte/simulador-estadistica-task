import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulador de Ejercicios de Estadística",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS completos para ocultar todo el marco de Streamlit
st.markdown("""
    <style>
        /* Oculta encabezado, menú superior y los 3 puntos */
        header, #MainMenu, [data-testid="stHeader"] {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* Oculta el footer y botones del desarrollador */
        footer, [data-testid="stStatusWidget"], .stActionButton, [data-testid="manage-app-button"] {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* Elimina márgenes blancos alrededor de la app */
        .block-container {
            padding: 0rem !important;
            margin: 0rem !important;
        }
        
        iframe {
            width: 100%;
            height: 100vh;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=950, scrolling=True)
