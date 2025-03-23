import streamlit as st
import pandas as pd
import plotly.express as xp

# Leemos el archivo csv
df_vehicles = pd.read_csv('vehicles_us.csv')
df_vehicles = df_vehicles.drop_duplicates()

# Creamos encabezado
st.header('Analisis de vehiculos')

hist_button = st.button('Construir histograma') # crear un botón para el histograma
disp_button = st.button('Construir gráfico de dispersión') # Crear botón para el gráfico de dispersión

        if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(df_vehicles, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)
            
        if disp_button: # al hacer click en el botón
            # escribir el mensaje
            st.write('creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')

            # Creamos el gráfico de dispersión
            fig = px.scatter(df_vehicles, x='odometer', y='price')

            # Mostramos un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)