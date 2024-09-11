import pandas as pd
import plotly.express as px
import streamlit as st
pd.set_option('display.max_columns', None)

car_data = pd.read_csv('vehicles_us.csv')

#Agregar un encabezado
st.header('Análisis Interactivo de anuncios de Coches')

#Crear botones para histogramas y gráficos de dispersión
boton_hist_1 = st.button('Construir histograma')  # Crear un botón para el histograma
boton_disp_1 = st.button('Construir gráfico de dispersión')  # Crear un botón para el gráfico de dispersión

#Acción al hacer clic en el botón para el histograma
if boton_hist_1:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

#Crear un histograma (ajustar la columna según tus datos)
    fig_hist = px.histogram(car_data, x='odometer')  # Reemplaza 'odometer' con la columna correcta si es necesario

#Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

#Acción al hacer clic en el botón para el gráfico de dispersión
if boton_disp_1:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

#Crear un gráfico de dispersión (ajustar columnas según tus datos)
    fig_scatter = px.scatter(car_data, x='odometer', y='price')  # Reemplaza 'odometer' y 'price' con las columnas correctas

#Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
