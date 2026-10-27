import streamlit as st
import requests

st.title("Clima en Chihuahua (Tiempo Real)")

# Consulta la API gratuita de Open-Meteo cada 10 minutos (600 segundos)
@st.cache_data(ttl=600)
def obtener_clima():
    # Coordenadas de Chihuahua: Lat 28.6353, Lon -106.0889
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.6353&longitude=-106.0889&current=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation"
    response = requests.get(url)
    return response.json()["current"]

# Obtenemos los datos actualizados
clima = obtener_clima()

# Extraemos los valores
temp = clima["temperature_2m"]
humedad = clima["relative_humidity_2m"]
viento = clima["wind_speed_10m"]
lluvia = clima["precipitation"]

# Mostramos las métricas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Temperatura", value=f"{temp} °C", icon="🌡️")

with col2:
    st.metric(label="Humedad", value=f"{humedad}%", icon="💧")

with col3:
    st.metric(label="Viento", value=f"{viento} km/h", icon="💨")

with col4:
    st.metric(label="Lluvia", value=f"{lluvia} mm", icon="🌧️")
