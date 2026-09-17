import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulador de Ejercicios de Estadística",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Estilos CSS avanzados para eliminar la marca de agua flotante e interfaz nativa
st.markdown("""
    <style>
        /* Oculta encabezados y menús superiores */
        [data-testid="stHeader"], header, #MainMenu {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* Oculta la insignia flotante verde de Streamlit y el pie de página */
        footer, 
        .stAppViewerFooter, 
        [data-testid="stStatusWidget"],
        [data-testid="stDecoration"],
        [data-testid="stToolbar"],
        div[class*="viewerBadge"],
        div[class*="stAppToolbar"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Ajuste de márgenes */
        .main .block-container {
            padding: 0rem !important;
            margin: 0rem !important;
            max-width: 100% !important;
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
