import streamlit as st

st.title("Clima en Chihuahua")

# Creamos 4 columnas para mostrar las métricas juntas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Temperatura",
        value="28 °C",
        delta="2 °C",
        icon="🌡️"
    )

with col2:
    st.metric(
        label="Humedad",
        value="45%",
        delta="-3%",
        icon="💧"
    )

with col3:
    st.metric(
        label="Viento",
        value="18 km/h",
        icon="💨"
    )

with col4:
    st.metric(
        label="Lluvia",
        value="10%",
        icon="🌧️"
    )
