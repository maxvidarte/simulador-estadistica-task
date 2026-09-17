import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulador de Ejercicios de Estadística",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS para ocultar encabezado, footer, ícono flotante de Streamlit y márgenes
st.markdown("""
    <style>
        /* Oculta la barra superior (menú, Fork, GitHub) */
        header {visibility: hidden !important;}
        #MainMenu {visibility: hidden !important;}
        
        /* Oculta el pie de página y los íconos/marcas de agua de Streamlit */
        footer {visibility: hidden !important;}
        .stAppViewerFooter {display: none !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        .stActionButton {display: none !important;}
        
        /* Ajusta los márgenes para pantalla completa sin espacios en blanco */
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
