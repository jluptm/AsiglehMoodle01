import streamlit as st
import pandas as pd
import mysql.connector

@st.cache_resource
def conectar_mysql():
    return mysql.connector.connect(
        host= '',
        port= 3306,
        user= '',
        password= '',
        database= '')

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
dataf = obtener_datos()
'dataf = '
dataf




