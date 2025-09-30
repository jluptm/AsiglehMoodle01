import streamlit as st
import pandas as pd
import mysql.connector

@st.cache_resource
def get_database_session(url):
    # Configuración de la conexión a la base de datos
    DB_CONFIG = {
        'host': '185.214.132.9',
        'user': 'u548971155_iQpBi',
        'password': '>BM#d|PAFV7v',
        'database': 'u548971155_srHVY'}
    #
    return DB_CONFIG
    
@st.cache_data
def load_data():
    DB_CONFIG = get_database_session('185.214.132.9')
    f"DB_CONFIG ====> {DB_CONFIG}"
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True) # dictionary=True para obtener resultados como diccionarios
        query = """SELECT ALL FROM pxqz_quiz_attemps AS qa"""
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return pd.DataFrame(data)
    except mysql.connector.Error as err:
        st.error(f"Error de conexión a la base de datos: {err}")
        return pd.DataFrame() # Devuelve un DataFrame vacío en caso de error

df = load_data()
df
# Asegúrate de que df no esté vacío antes de continuar
# if not df.empty:
#     st.title("Dashboard de Cuestionarios Moodle")

#     st.header("Notas por Cuestionario y Estudiante")
#     st.dataframe(df)

#     st.header("Histograma de Notas por Cuestionario")
    
#     for cuestionario in df['Cuestionario'].unique():
#         st.subheader(f"Histograma para: {cuestionario}")
#         df_cuestionario = df[df['Cuestionario'] == cuestionario]
        
#         if not df_cuestionario.empty:
#             # Crea el histograma de notas
#             st.bar_chart(df_cuestionario['Calificacion'].value_counts().sort_index())
#         else:

#             st.write("No hay datos para este cuestionario.")









