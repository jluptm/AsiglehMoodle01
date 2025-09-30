import streamlit as st
import pandas as pd
import mysql.connector

@st.cache_resource
def conectar_mysql():
    return mysql.connector.connect(
        host= '185.214.132.9',
        port= 3306,
        user= 'u548971155_iQpBi',
        password= '',
        database= 'u548971155_srHVY')

@st.cache_data
def obtener_datos():
    conn = conectar_mysql()
    query = """SELECT ALL FROM pxqz_quiz_attemps AS qa"""
    df = pd.read_sql(query, conn)
    conn.close()
    #cursor.execute(query)
    #data = cursor.fetchall()
    #cursor.close()
    #conn.close()
    return df

'df = '
df




