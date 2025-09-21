import streamlit as st
import streamlit_antd_components as sac
from PIL import Image
import time

st.session_state['wi'] = 'home2025'
st.session_state['wo'] = None # Limpiar 'wo' al inicio para asegurar flujo correcto

st.set_page_config(
    page_title="EduASIGLEH App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Cargar imágenes una sola vez al inicio de la aplicación
#imagen1 = Image.open('minecLogo.jpeg')
#imagen2 = Image.open('minecLogoTitle.jpeg')
#imagen3 = Image.open('MINEC4.jpg')
# 1. Leer los parámetros de la URL
params = st.query_params
idpag = params.get("idpag")
fecha = params.get("fecha")

def limpiasessionst():
    """Limpia variables de sesión específicas para evitar conflictos entre páginas."""
    keys_to_clear = [
        'nombres', 'apellidos', 'df3', 'df1', 'dfpagos', 'fileup',
        'usuarioAdm', 'usad', 'dtto', 'pagina', 'totalreg', 'conseguirRegistros',
        'xi', 'xf', 'todosLosReg', 'iglesiasLinked', 'lastemail', 'bdatage',
        'telefonos', 'zona', 'categoria', 'registromin', 'logina', 'cedula',
        # Nuevas variables de sesión para el Diálogo Educativo y Administración
        'cedula_dialogo', 'datos_personales_de', 'datos_eclesiasticos_de',
        'datos_pago_de', 'current_dialogo_record', 'current_pagosde_record',
        'matriculacion_status', 'transferencias_df', 'pagos_de_df',
        'matching_df', 'file_uploaded_admin', 'logina', 'usad'
    ]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]

# Inicializar o limpiar variables de sesión en el flujo principal
if 'Acceso' not in st.session_state:
    st.session_state['Acceso'] = 'Principal' # Estado inicial de la aplicación
    limpiasessionst() # Asegurar una limpieza al inicio de la sesión

# --- Pantalla Principal ---
if st.session_state['Acceso'] == 'Principal':
    #
    # st.image(imagen3) # Mostrar imagen de bienvenida

    # Título o mensaje de bienvenida
    #st.markdown("<h3 style='text-align: center; color: #f9f5f6;'>Bienvenido al Sistema de Registro MINEC</h3>", unsafe_allow_html=True)
   
    # Contenedor para los botones principales
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2: # Centrar los botones en la columna del medio
        st.subheader("Bienvenido")
        st.write("") # Espacio para centrado visual
        st.subheader('Ingresar')
        with st.form('Login'):
            usuario = st.text_input('Usuario', placeholder='nombre de usuario')
            clave = st.text_input('Clave de acceso', type="password", placeholder='clave de acceso')
            enviar = st.form_submit_button('Acceder')
        st.code(f"idpag : {idpag}  /  fecha : {fecha}")
        